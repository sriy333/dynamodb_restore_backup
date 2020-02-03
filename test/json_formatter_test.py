
import unittest
from dynamodb import json_formatter


class JsonFormatterTest(unittest.TestCase):

    def test_opening_file(self):
        store = json_formatter.JsonFormatter.login_via_cli(self,"C:/Users/z003u7pv/data.json")


    def test_range_check(self):
        store = json_formatter.JsonFormatter.fetching_from_file("C:/Users/z003u7pv/export.json")

    def test_fetch_data_from_db(self):
        json_formatter.JsonFormatter.fetching_data_from_dynamodb(self)

if __name__ == '__main__':
    unittest.main()
