import csv
import platform
import os
import sys
import math
from pathlib import Path
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, FAAPATH)
import src.utils as utils

def write_result_csv(faa_obj, out_fp):
    resultsf = os.path.join(out_fp,'results.csv')
    with open(resultsf, 'w', newline='') as outpath:
        out_writer = csv.writer(outpath, dialect='excel', delimiter=',')
        out_writer.writerow(["Structure", "Need to File?"])
        for i in range(len(faa_obj.names)):
            out_writer.writerow([faa_obj.names[i], faa_obj.results[i]])

def write_webfiles(faa_obj, out_fp):
    # Write result web pages
    for i in range(len(faa_obj.pages)):
        page_fp = local_path(out_fp, faa_obj.names[i], ".html")
        with open(page_fp, 'w') as outpath:
            outpath.write(faa_obj.pages[i])
    # Write result reference pages - JS and CSS
    # TODO: need to handle images separately with 'wb'
    # TODO: add directory creation when ./oeaaa/external/css or ./oeaaa/external/image does not exist
    for i in range(len(faa_obj.ref_pages)):
        #filter out the common path so the ref file can go to a subdirectory
        common_path = os.path.commonpath(
                [faa_obj.url, faa_obj.ref_links[i].url])
        ref_path = os.path.dirname(faa_obj.ref_links[i].url[len(common_path)+2:])
        ref_path = os.path.join(out_fp, "oeaaa", "external", ref_path)
        page_fp = local_path(ref_path, faa_obj.ref_links[i].url, "")
        with open(page_fp, 'w') as outpath:
            outpath.write(faa_obj.ref_pages[i])

def local_path(path, file_name, *args):
    parse_fn = os.path.basename(file_name)
    res = os.path.join(path, parse_fn + args[0])
    return res