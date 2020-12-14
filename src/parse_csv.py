import csv
import platform
import os
import sys
import math
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, FAAPATH)
import src.utils as utils
# Parse csv file into a format suitable for the faa site.
# As the csv row is imported, process each piece of data
def readcsv(in_file):
    tmp_list = []
    with open(in_file, newline='') as csvfile:
        in_reader = csv.reader(csvfile, delimiter=',')
        # skip header row
        next(in_reader)
        # process the temporary list data item by item
        # each list entry is a dictionary tagged with the web form ids
        for row in in_reader:
            structure_des = utils.sanitize_des(str(row[0]), platform.platform()) # structure designation
            lat = utils.coord_to_dms(row[1], "lat") # latitude
            longitude = utils.coord_to_dms(row[2], "long") # longitude
            datum = row[3].strip()
            # TODO: build an option for rounding
            ele = round(float(row[4])) # site elevation (ft)
            str_ht = math.ceil(float(row[5])) # structure height (ft)
            traverseway = row[6].strip() # Traverseway
            if row[7].strip() == 'Yes':
                on_airport = "true" # Is on airport?
            else:
                on_airport = "false"
            tmp_list.append(
                {"str_desc": structure_des,
                    "latD": lat[0],"latM": lat[1],"latS": lat[2],"latDir": lat[3],
                    "longD": longitude[0],"longM": longitude[1],"longS": longitude[2],"longDir": longitude[3],
                    "datum": datum,
                    "siteElevation": ele,
                    "unadjustedAgl": str_ht,
                    "traverseway": traverseway,
                    "onAirport": on_airport})
    return tmp_list