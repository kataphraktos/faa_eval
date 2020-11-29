import unittest
import os
import sys
TESTPATH = os.path.dirname(os.path.abspath(__file__))
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, FAAPATH)
from src import utils, faa_web

class Test_web_response(unittest.TestCase):
    def test_web(self):
        Test_CSVres = [
                {"str_desc": "1",
                "latD": "60", "latM": "30", "latS": "25.53", "latDir": "N",
                "longD": "103", "longM": "35", "longS": "35.0", "longDir": "W",
                "datum": "NAD83",
                "siteElevation": "56",
                "unadjustedAgl": "201",
                "traverseway": "No Traverseway",
                "onAirport": "false"},
                {"str_desc": "1_1",
                "latD": 50, "latM": 45, "latS": "17.59", "latDir": "S",
                "longD": 103, "longM": 20, "longS": "18.75", "longDir": "E",
                "datum": "NAD83",
                "siteElevation": 700,
                "unadjustedAgl": 151,
                "traverseway": "No Traverseway",
                "onAirport": "false"},
                {"str_desc": "Turbine #3",
                "latD": 30,"latM": 27,"latS": "12.64", "latDir": "S",
                "longD": 97, "longM": 53, "longS": "28.82", "longDir": "W",
                "datum": "NAD27",
                "siteElevation": 1001,
                "unadjustedAgl": 500,
                "traverseway": "Public Roadway",
                "onAirport": "false"}]
        test = faa_web.faa_web(Test_CSVres)
        self.assertEqual(["Yes", "No", "Yes"], test.results)

if __name__ == '__main__':
    unittest.main()