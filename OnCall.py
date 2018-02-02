import time
import datetime
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OnCall:
    """Class that changes on call in web browser
    For oncall users."""

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Firefox(executable_path=r'C:\\geckodriver\\geckodriver.exe')
        self.numbers = []

    def load_web_browser(self, user, passwd):
        """Loads web browser web page"""
        self.browser.get(self.url)
        time.sleep(1)

        username = self.browser.find_element_by_name("j_username")
        password = self.browser.find_element_by_name("j_password")

        username.send_keys(user)
        password.send_keys(passwd)

        login = self.browser.find_element_by_xpath("//div[@class='loginButton']")
        login.click()
        time.sleep(3)

    def change_oncall_number(self, number, date):
        """Changes the oncall number based on date."""
        self.numbers.append(number)

        oncall = self.browser.find_element_by_name("cfaslect")
        oncall.clear()
        oncall.send_keys(number[1])

        save = self.browser.find_element_by_id("btnSave_label")
        save.click()
        self.browser.close()
        sys.exit()