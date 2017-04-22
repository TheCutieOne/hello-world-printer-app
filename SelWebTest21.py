import unittest
from selenium import webdriver
from time import sleep

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session

        self.driver = webdriver.Chrome()
        driver = self.driver
        # driver.implicitly_wait(30)
        driver.maximize_window()
        # navigate to the application home page
        driver.get("http://www.wsb.pl/")

    def test_search_by_text(self):
        driver = self.driver
        # get the search textbox
        link = driver.find_element_by_css_selector("#block-menu-menu-wybierz-studia-w-wsb > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
        link.click()
        sleep(5)
        link = driver.find_element_by_css_selector(".lmenu-first > li:nth-child(7) > a:nth-child(1)")
        link.click()
        sleep(5)

    def test_search_by_text2(self):
        driver = self.driver
        # get the search textbox
        link = driver.find_element_by_css_selector("#block-menu-menu-wybierz-studia-w-wsb > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")
        link.click()
        sleep(5)
        link = driver.find_element_by_css_selector("#menu-o-uczelni")
        link.click()
        sleep(5)

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
