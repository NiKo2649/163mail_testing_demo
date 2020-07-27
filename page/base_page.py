# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 1:16
# @Author : NiKo
# @File : base_page.py
# @Software: PyCharm
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from tools.config_parser import ConfigParser

p = ConfigParser("config.ini")


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.by = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.timeout = 15

    def find_element(self, by, path):
        try:
            element = wait(self.driver, self.timeout).until(lambda x:x.find_element(by, path))
        except exceptions.TimeoutException as t:
            print(t)
        else:
            return element

    def refresh(self):
        self.driver.refresh()

    def del_cookies(self):
        self.driver.delete_all_cookies()

    def open_url(self):
        self.driver.get(p.get("base", "test_url"))

    def is_element_exist(self, b, path):
        try:
            wait(self.driver, self.timeout). \
                    until(conditions.visibility_of_element_located((self.by[b], path)))
        except exceptions.TimeoutException:
            return False
        return True





