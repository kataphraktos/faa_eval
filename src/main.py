# combine csv and web parsing in a user interface. print results
import os
import sys
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, FAAPATH)
import src.faa_web as faa_web
import src.parse_csv as parse_csv
import src.print_file as print_file


def console_run():
    if len(sys.argv) == 1:
        csv_fp = input("Enter the name or path with name to the CSV: ")
        out_fp = input("Enter the file path where results will be saved: ")
    elif len(sys.argv) == 3:
        csv_fp = sys.argv[1]
        out_fp = sys.argv[2]
    else:
        print("Error: incorrect number of arguments. Call function with two arguments: csv_file, out_file")
    # if a filename is passed as the csv, use the console working directory
    if os.path.isfile(csv_fp):
        dir_path = os.getcwd()
        csv_fp = os.path.join(dir_path, csv_fp)
    # if no out filepath is specified, use the csv directory
    if out_fp == "":
        out_fp = os.path.dirname(csv_fp)
    print("Reading CSV data...")
    parsed_data = parse_csv.readcsv(csv_fp)
    print("Processing web results...")
    faa_obj = faa_web.faa_web(parsed_data)
    print("Writing structure results to disk...")
    print_file.write_result_csv(faa_obj, out_fp)
    print("Writing structure maps to disk...")
    print_file.write_webfiles(faa_obj, out_fp)
    print("FAA data written to: " + out_fp +
            "\nProcessed " + str(len(faa_obj.pages)) + " structures")


if __name__ == '__main__':
    console_run()