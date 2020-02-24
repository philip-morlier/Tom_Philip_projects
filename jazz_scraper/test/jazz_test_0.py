import unittest
import requests
from src.NprScraper import *



class MyTestCase(unittest.TestCase):
    url = 'https://api.composer.nprstations.org/v1/widget/519298c7e1c876ffebb2149b/day?date=2020-02-01&format=html'

    def test_get(self):
        page = requests.get(self.url)
        self.assertIsNotNone(page)

    def test_parse(self):
        page = requests.get(self.url)
        pp = NprScraper()
        pp.parse(page)
        self.assertIsNotNone(pp)




if __name__ == '__main__':
    unittest.main()
