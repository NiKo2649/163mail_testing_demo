# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 12:06
# @Author : NiKo
# @File : login_page.py
# @Software: PyCharm
from selenium import webdriver
from page.base_page import BasePage
from tools.config_parser import ConfigParser
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.common import exceptions

s = "login_page"
p = ConfigParser("data/UIMap.ini")


class LoginPage(BasePage):
    def login(self, account, pasword):
        try:
            wait(self.driver, 10). \
                until(conditions.frame_to_be_available_and_switch_to_it((p.get(s, "login_frame_by"),
                                                                         p.get(s, "login_frame_path"))))
        except exceptions.TimeoutException as t:
            print('error: found  timeout！切换frame失败')
        email = self.find_element(self.by[p.get(s, "email_input_by")],
                                    p.get(s, "email_input_path"))
        email.clear()
        email.send_keys(account)
        password = self.find_element(self.by[p.get(s, "password_input_by")],
                                                p.get(s, "password_input_path"))
        password.clear()
        password.send_keys(pasword)
        self.find_element(self.by[p.get(s, "login_button_by")],
                                    p.get(s, "login_button_path")).click()

    def is_login_failed(self):
        try:
            wait(self.driver, self.timeout).\
                until(lambda x: x.find_element_by_xpath("//div[contains(@title,'帐号或密码错误')]"))
        except exceptions.TimeoutException:
            return False
        return True

    def is_login_succeed(self):
        return conditions.title_contains("网易邮箱6.0版")


