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
        South_res = [65, 30, 48.60, "S"]
        self.assertEqual(utils.coord_to_dms("-65.5135", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("65.5135S", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("65d30'48.6\"S", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("-65d30'48.6\"", "lat"), South_res)
    def test_Wformats(self):
        West_res = [103, 15, 55.68, "W"]
        self.assertEqual(utils.coord_to_dms("-103.265466667", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("103.265466667W", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("103 d 15'55.68\"W", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("-103 d 15'55.68\"", "long"), West_res)
    def test_other_directions(self):
        self.assertEqual(utils.coord_to_dms("85", "lat"),
                [85, 0, 0.00, "N"])
        self.assertEqual(utils.coord_to_dms("103.265466667", "long"),
                [103, 15, 55.68, "E"])

class Test_parse_csv(unittest.TestCase):
    def test_import(self):
        Test_CSVres = [
                {"str_desc": "1",
                "latD": -5, "latM": 30, "latS": 25.53, "latDir": "N",
                "longD": 103, "longM": 35, "longS": 35.0, "longDir": "W",
                "datum": "NAD83",
                "siteElevation": 56,
                "unadjustedAgl": 201,
                "traverseway": "No Traverseway",
                "onAirport": False},
                {"str_desc": "1_1",
                "latD": 50, "latM": 45, "latS": 17.59, "latDir": "S",
                "longD": 103, "longM": 20, "longS": 18.75, "longDir": "E",
                "datum": "NAD83",
                "siteElevation": 700,
                "unadjustedAgl": 151,
                "traverseway": "No Traverseway",
                "onAirport": False},
                {"str_desc": "Turbine #3",
                "latD": 30,"latM": 27,"latS": 12.64, "latDir": "S",
                "longD": 97, "longM": 53, "longS": 28.82, "longDir": "W",
                "datum": "NAD27",
                "siteElevation": 1001,
                "unadjustedAgl": 500,
                "traverseway": "Public Roadway",
                "onAirport": False}]
        test_csv_path = os.path.join(TESTPATH,"test_data_csv.csv")
        self.assertEqual(parse_csv.readcsv(test_csv_path), Test_CSVres)

if __name__ == '__main__':
    unittest.main()