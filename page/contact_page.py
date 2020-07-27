# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 12:06
# @Author : NiKo
# @File : contact_page.py
# @Software: PyCharm
from page.base_page import BasePage
from tools.config_parser import ConfigParser

s = "contact_page"
p = ConfigParser("data/UIMap.ini")


class ContactPage(BasePage):
    def switch_to_contact(self):
        self.find_element(self.by[p.get(s, "switch_button_by")],
                           p.get(s, "switch_button_path")).click()

    def add_new_contact(self, name, email, ifstar, tel, other):
        self.switch_to_contact()
        self.find_element(self.by[p.get(s, "new_contact_button_by")],
                                    p.get(s, "new_contact_button_path")).click()
        self.find_element(self.by[p.get(s, "name_input_by")],
                          p.get(s, "name_input_path")).send_keys(name)
        self.find_element(self.by[p.get(s, "email_input_by")],
                          p.get(s, "email_input_path")).send_keys(email)
        self.find_element(self.by[p.get(s, "tel_input_by")],
                          p.get(s, "tel_input_path")).send_keys(tel)
        self.find_element(self.by[p.get(s, "other_input_by")],
                          p.get(s, "other_input_path")).send_keys(other)
        if ifstar == '1':
            self.find_element(self.by[p.get(s, "if_star_by")],
                              p.get(s, "if_star_path")).click()
        self.find_element(self.by[p.get(s, "confirm_button_by")],
                          p.get(s, "confirm_button_path")).click()




