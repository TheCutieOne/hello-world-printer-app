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
        driver.get("https://wizzair.com/pl-pl/main-page#/")

    def test_search_by_text(self):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element_by_id("lst-ib")
        search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("Selenium")
        sleep(5)
        search_field.submit()

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
