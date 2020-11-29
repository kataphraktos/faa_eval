# This object:
# Opens the faa webpage, ingests parsed csv data, and returns an HTML page
# for each entry in the csv. The referenced files for the first csv are also
# downloaded.

from urllib.parse import urljoin
import requests
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
SRCPATH = os.path.dirname(os.path.abspath(__file__))
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SRCPATH)
from utils import FORM_IDS

## Unfortunately, the site uses JS to tweak the agl height, so a solution
# with mechanicalsoup is not possible
""" import mechanicalsoup
browser = mechanicalsoup.Browser()
page = browser.get(url).soup
latD = page.find(id="latD")

page.find(id="latM")
page.find(id="latS")
page.find(id="latDir")
page.find(id="longD")s
page.find(id="longM")
page.find(id="longS")
page.find(id="longDir")
page.find(id="datum")
page.find(id="siteElevation")
page.find(id="unadjustedAgl")
page.find(id="traverseway")
page.find(id="onAirport")
first_200 = True
# use mechanicalsoup to get each web page
browser = mechanicalsoup.StatefulBrowser()
browser.open(URL)
browser.select_form()
for i in range(len(arglist)):
    for form_id in FORM_IDS:
        browser[form_id] = arglist[i][form_id]
    postreply = browser.submit_selected()
    if postreply.status_code == 200:
        if first_200:
            first_200 = False
            for ref in postreply.soup.find_all("link"):
                ref_links.append(requests.get(urljoin(URL, ref.attrs.get("href"))))
        resp.append(postreply)
    else:
        resp.append('0')
 """


class faa_web:

    def __init__(self, arglist):
        URL = "https://oeaaa.faa.gov/oeaaa/external/gisTools/gisAction.jsp?action=showNoNoticeRequiredToolForm"
        resp = []
        names = []
        self.url = URL
        # TODO: add error handling
        driver = webdriver.Chrome(executable_path=os.path.join(FAAPATH, 'chromedriver')) #chrome_options=chromeoptions)
        driver.get(URL)
        for i in range(len(arglist)):
            for form_id in FORM_IDS:
                ele = driver.find_element_by_id(form_id)
                if ele.tag_name == "select":
                    select_ele = Select(driver.find_element_by_id(form_id))
                    select_ele.select_by_visible_text(arglist[i][form_id])
                elif ele.get_attribute('value') == arglist[i][form_id]:
                    ele.click()
                else:
                    ele.clear()
                    ele.send_keys(arglist[i][form_id])
            ele.send_keys(Keys.RETURN)
            resp.append(driver.page_source)
        self._resp = resp
        # TODO: use ref_links in page output
        for i in range(len(arglist)):
            names.append(arglist[i].get("str_desc"))
        self.names = names

        self.ref_links = self.scrape_links()
        self.results = self.scrape_result()
        driver.quit()

    def get_web(self, arglist):
        pass

    def scrape_result(self):
        res = []
        for html_resp in self._resp:
            resp_soup = BeautifulSoup(html_resp, 'html.parser')
            if "The FAA requests that you file" in resp_soup.text:
                res.append("Yes")
            else:
                res.append("No")
        return res

    def scrape_links(self):
        # Pull the links for only the first entry; the rest should be the same
        ref_links = []
        resp_soup = BeautifulSoup(self._resp[0], 'html.parser')
        for ref in resp_soup.find_all("link"):
            ref_links.append(
                requests.get(urljoin(self.url,ref.attrs.get("href"))))
        return ref_links