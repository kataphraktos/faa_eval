import csv
import platform
import os
import io
import sys
import math
from PIL import Image
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
    # make reference page directories if they don't exist
    _refs_mkdirs(out_fp,
            [["oeaaa", "external"],
            ["oeaaa", "external", "maps"],
            ["oeaaa", "external", "images", "layout"],
            ["oeaaa", "external", "include", "css"]])
    # Write reference pages - JS and CSS
    for i in range(len(faa_obj.ref_pages)):
        # filter out the common path so the ref file can go to a subdirectory
        common_path = os.path.commonpath(
                [faa_obj.url, faa_obj.ref_links[i].url])
        ref_path = os.path.dirname(faa_obj.ref_links[i].url[len(common_path)+2:])
        ref_path = os.path.join(out_fp, "oeaaa", "external", ref_path)
        ref_file = os.path.basename(faa_obj.ref_links[i].url)
        page_fp = local_path(ref_path, ref_file, "")
        if(
            ".png" in ref_file or
            ".ico" in ref_file or
            ".gif" in ref_file
            ):
            #remove addressing after filename if present (mapped pngs)
            if ref_file.find(".")+4 != len(ref_file):
                ref_file = ref_file[:ref_file.find(".")+4]
                page_fp = local_path(ref_path, ref_file, "")
            ref_img = Image.open(io.BytesIO(faa_obj.ref_links[i].content))
            ref_img = ref_img.save(page_fp)
        else:
            with open(page_fp, 'w') as outpath:
                outpath.write(faa_obj.ref_pages[i])

def local_path(path, file_name, *args):
    parse_fn = os.path.basename(file_name)
    res = os.path.join(path, parse_fn + args[0])
    return res

def _refs_mkdirs(out_fp, sub_dirs):
    for sub_dir in sub_dirs:
        forward_path = out_fp
        for i in range(len(sub_dir)):
            forward_path = os.path.join(forward_path, sub_dir[i])
        tmp_path = forward_path
        if not os.path.isdir(tmp_path):
            Path(tmp_path).mkdir(parents=True, exist_ok=True)