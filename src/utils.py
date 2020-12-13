# misc. utilities for the program
import math


# Convert the latitude or longitude coordinate into a useable DMS object with direction.
# The coordinate format may be one of four options, best shown by example:
# these four inputs:
# (-65.5135, lat), (65d30'48.6"S, lat), (65.5135S, lat), (-65d30'48.6", lat)
# all produce the same DMS object: [65, 30, 48.6, "S"]
# 
# The function processes the coord data to extract relevant information by trimming a
# copy of coord
def coord_to_dms(coord, lat_or_long):
    tmp_dms = [0,0,0,""]
    proc_coord = coord
    proc_coord = proc_coord.replace(' ', '')
    # relate negative and positive values to a cardinal direction check
    if lat_or_long == "lat":
        is_south = ((proc_coord.startswith("-") or proc_coord.endswith("S"))
                and not proc_coord.endswith("N"))
    else:
        is_west = ((proc_coord.startswith("-") or proc_coord.endswith("W"))
                and not proc_coord.endswith("E"))
    # assign direction based on direction check
    if lat_or_long == "lat":
        if is_south:
            tmp_dms[3] = "S"
        else:
            tmp_dms[3] = "N"
    else:
        if is_west:
            tmp_dms[3] = "W"
        else:
            tmp_dms[3] = "E"
    if proc_coord.startswith("-"):
        proc_coord = proc_coord[1:]
    elif (proc_coord.endswith("N") or proc_coord.endswith("S") or
            proc_coord.endswith("E") or proc_coord.endswith("W")):
        proc_coord = proc_coord[:-1]
    else:
        pass #error handling
    # determine the numeric format
    if ((proc_coord.find("d") == -1) and (proc_coord.find("d") == -1)):
        num_form = "dec"
    else:
        num_form = "dms"
    # process based on numeric format
    if num_form == "dec":
        proc_coord = float(proc_coord)
        tmp_D = math.floor(proc_coord)
        tmp_M = math.floor((proc_coord - tmp_D)*60)
        tmp_S = round(((proc_coord - tmp_D)*60 -tmp_M)*60,2)
        tmp_dms[0] = int(tmp_D)
        tmp_dms[1] = int(tmp_M)
        tmp_dms[2] = tmp_S
    else:
        i = 0
        for sep in ["d", "'", '"']:
            tmp_split = proc_coord.split(sep)
            proc_coord = tmp_split[1]
            if i == 2:
                tmp_dms[i] = float(tmp_split[0])
            else:
                tmp_dms[i] = int(tmp_split[0])
            i += 1
    return tmp_dms

# Sanitize the structure description of illegal file name characters.
# Characters for both Windows and Unix are converted to "_"
def sanitize_des(str_des, platform):
    tmp_res = str_des.strip()
    if "Windows" in platform:
        for illegal_char in ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]:
            tmp_res = tmp_res.replace(illegal_char,"_")
    else:
        tmp_res = tmp_res.replace("/", "_")
    return tmp_res

# Remove characters after a png map image name to save locally
def local_map(ref_name):
    if ref_name.find(".")+4 != len(ref_name):
        return ref_name[:ref_name.find(".")+4]
    else:
        return ref_name

FORM_IDS = [
        "latD",
        "latM",
        "latS",
        "latDir",
        "longD",
        "longM",
        "longS",
        "longDir",
        "datum",
        "siteElevation",
        "unadjustedAgl",
        #"structureHeight",
        "traverseway",
        "onAirport"
        ]