import unittest
from selenium import webdriver
from time import sleep

"""
Get "http://wp.pl" startpage
Check if there is a specific word
Check if more that one
"""

search_word = "na"

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()

    def test_search_by_word_na(self):
        driver = self.driver
        driver.get("http://www.wp.pl")
        results = driver.find_elements_by_xpath('//div[contains(text(),"' + search_word +'")]')
        for r in results:
            print(r.text)
        self.assertGreater(len(results), 1)
    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
