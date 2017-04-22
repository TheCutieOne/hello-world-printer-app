import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

valid_username = "testerwsb_t1"
valid_password = "adam1234"
search_word = "podany"
"""
Open page wp.pl
Go to "poczta"
Login to user "testerwsb_t1"
Password "adam1234"
Chceck if there is a word "Odebrane"
Do the same with wrong password
Do the same with the wrong user
Do the same with wrong password and user
"""

class WPplSearch(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()

    def test_mail(self):
        driver = self.driver
        driver.get("http://www.wp.pl")
        driver.find_element_by_css_selector("._3fCp7 > li:nth-child(1) > a:nth-child(1)").click()
        search_field = driver.find_element_by_id("login")
        search_field.send_keys(valid_username)
        search_field = driver.find_element_by_id("password")
        search_field.send_keys(valid_password)
        link = driver.find_element_by_id('btnSubmit').click()
        sleep(2)
        driver.find_element_by_css_selector('html body.hasCollapsers.dragdrop-dropTarget.dragdrop-boundary div#main div#middle div#leftColumn div#leftColumnInner.inner table.dragdrop-dropTarget tbody tr td div.boxContainer.dragdrop-draggable div.boxContent table.foldersTreeContainer tbody tr td div.foldersList table tbody tr td table.GNNS3A-NK.GNNS3A-FK tbody tr td.GNNS3A-JK.activeFolderLabel table.GNNS3A-IK.boldTxt tbody tr td a.gwt-Anchor').click()
        sleep(2)
        link = driver.find_element_by_css_selector('html body.hasCollapsers.dragdrop-dropTarget.dragdrop-boundary div#header div#headerWrapper div#userMenu div#buttonLogout.btn a').click()

    def test_mail1(self):
        driver = self.driver
        driver.get("http://www.wp.pl")
        driver.find_element_by_css_selector("._3fCp7 > li:nth-child(1) > a:nth-child(1)").click()
        search_field = driver.find_element_by_id("login")
        search_field.send_keys(valid_username)
        search_field = driver.find_element_by_id("password")
        search_field.send_keys("546515641684")
        link = driver.find_element_by_id('btnSubmit').click()
        sleep(2)
        search_field = driver.find_element_by_id("login").clear()
        search_field = driver.find_element_by_id("password").clear()
        sleep(2)
        search_field = driver.find_element_by_id("login")
        search_field.send_keys("pazdzioch")
        search_field = driver.find_element_by_id("password")
        search_field.send_keys(valid_password)
        link = driver.find_element_by_id('btnSubmit').click()
        sleep(2)
        search_field = driver.find_element_by_id("login").clear()
        search_field = driver.find_element_by_id("password").clear()
        sleep(2)
        search_field = driver.find_element_by_id("login")
        search_field.send_keys("pazdzioch")
        search_field = driver.find_element_by_id("password")
        search_field.send_keys("123456789134597441525")
        link = driver.find_element_by_id('btnSubmit').click()
        sleep(2)
        search_field = driver.find_element_by_id("login").clear()
        search_field = driver.find_element_by_id("password").clear()


    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
