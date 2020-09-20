#unit tests for parsing csvs and related functions

import unittest
import os
import sys
TESTPATH = os.path.dirname(os.path.abspath(__file__))
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, FAAPATH)
from src import utils, parse_csv

class Test_coord_to_dms(unittest.TestCase):
    def test_Sformats(self):
        South_res = [65, 30, 48.60000, "S"]
        self.assertEqual(utils.coord_to_dms("-65.5135", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("65.5135S", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("65d30'48.6\"S", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("-65d30'48.6\"", "lat"), South_res)
    def test_Wformats(self):
        West_res = [103, 15, 55.67983, "W"]
        self.assertEqual(utils.coord_to_dms("-103.2654666194", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("103.2654666194W", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("103 d 15'55.67983\"W", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("-103 d 15'55.67983\"", "long"), West_res)
    def test_other_directions(self):
        self.assertEqual(utils.coord_to_dms("85", "lat"),
                [85, 0, 0.00000, "N"])
        self.assertEqual(utils.coord_to_dms("103.2654666194", "long"),
                [103, 15, 55.67983, "E"])

class Test_parse_csv(unittest.TestCase):
    def test_import(self):
        Test_CSVres = [
                ["1", [88,30,25.528,"N"], [103,35,35.0,"W"], "NAD83",
                56, 201, "No Traverseway", "No"],
                ["1_1", [90,45,17.5891,"S"], [103,20,18.75,"E"], "NAD83",
                700, 151, "No Traverseway", "No"],
                ["Turbine #3", [85,27,12.636,"S"], [97,53,28.824,"W"], "NAD27",
                1001, 500, "Public Roadway", "No"]]
        test_csv_path = os.path.join(TESTPATH,"test_data_csv.csv")
        self.assertEqual(parse_csv.readcsv(test_csv_path), Test_CSVres)

if __name__ == '__main__':
    unittest.main()