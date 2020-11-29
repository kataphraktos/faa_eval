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

class faa_web:

    def __init__(self, arglist):
        URL = "https://oeaaa.faa.gov/oeaaa/external/gisTools/gisAction.jsp?action=showNoNoticeRequiredToolForm"
        names = []
        pages = []
        self.url = URL
        # TODO: add error handling
        self._resp = self._get_faa_web(arglist)
        # TODO: use ref_links in page output
        for i in range(len(arglist)):
            names.append(arglist[i].get("str_desc"))
        self.names = names
        for entry in self._resp:
            pages.append(BeautifulSoup(entry, 'html.parser').prettify())
        self.pages = pages
        self.ref_links = self._scrape_links()
        self.ref_pages = self._get_ref_web()
        self.results = self._scrape_result()

    def _get_faa_web(self, arglist):
        resp = []
        driver = webdriver.Chrome(executable_path=os.path.join(FAAPATH, 'chromedriver'))
        driver.get(self.url)
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
        driver.quit()
        return resp

    def _get_ref_web(self):
        resp = []
        driver = webdriver.Chrome(executable_path=os.path.join(FAAPATH, 'chromedriver'))
        for ref_link in self.ref_links:
            driver.get(ref_link.url)
            resp.append(BeautifulSoup(driver.page_source, 'html.parser').prettify())
        driver.quit()
        return resp

    def _scrape_result(self):
        res = []
        for html_resp in self._resp:
            resp_soup = BeautifulSoup(html_resp, 'html.parser')
            if "The FAA requests that you file" in resp_soup.text:
                res.append("Yes")
            else:
                res.append("No")
        return res

    def _scrape_links(self):
        # Pull the links for only the first entry; the rest should be the same
        ref_links = []
        resp_soup = BeautifulSoup(self._resp[0], 'html.parser')
        for ref in resp_soup.find_all("link"):
            ref_links.append(
                requests.get(urljoin(self.url,ref.attrs.get("href"))))
        return ref_links