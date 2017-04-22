# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

valid_name = "Dick"
valid_surname = "Laurent"
telefon = "123123123"
invalid_email = "hhjkj.pl"
valid_password = "Qshiukk12"


class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_registration_wrong_email(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        zaloguj_btn = driver.find_element_by_css_selector("#app > header > div > nav > ul > li:nth-child(3) > button")
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        rejestracja_btn.click()
        #imie_field =  driver.find_element_by_css_selector("#registration-modal > \
        #form > div.modal-popup__content.register-form__content > div.register-form__name-field > \
        #div.input-set__container.register-form__name-field__input.register-form__name-field__input--first > input")
        imie_field = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        imie_field.send_keys(valid_name)
        nazwisko_field = driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        nazwisko_field.send_keys(valid_surname)
        gender_switch = driver.find_element_by_id("register-gender-male")
        driver.execute_script("arguments[0].click()", gender_switch)
        #gender_switch = driver.find_element_by_css_selector('div[class="switch switch--gender switch--full-width gutter-bottom"] label[for=register-gender-male]')
        #gender_switch.click()
        telefon_field = driver.find_element_by_css_selector("input[type=tel]")
        telefon_field.send_keys(telefon)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
