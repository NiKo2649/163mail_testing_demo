# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 16:14
# @Author : NiKo
# @File : contact_test.py
# @Software: PyCharm

import pytest
from tools.excel_parser import ExcelParser
e = ExcelParser()
sheet = e.get_all_values_of_sheet(e.get_sheet_by_name("contact"))


class TestContact(object):

    @pytest.mark.parametrize('name, email, ifstar, tel, other', [sheet[0]])
    def test_contact_add_succeed(self, had_login, refresh_page, name, email, ifstar, tel, other):
        contact_page = had_login
        contact_page.switch_to_contact
        contact_page.add_new_contact(name, email, ifstar, tel, other)
        actual = contact_page.is_element_exist("xpath", "//span[contains(text(),'请正确填写邮件地址。')]")
        assert ~actual

    @pytest.mark.parametrize('name, email, ifstar, tel, other', [sheet[1]])
    @pytest.mark.xfail()
    def test_contact_add_failed(self, had_login, refresh_page, name, email, ifstar, tel, other):
        contact_page = had_login
        contact_page.switch_to_contact
        contact_page.add_new_contact(name, email, ifstar, tel, other)
        assert contact_page.is_element_exist("xpath", "//span[contains(text(),'请正确填写邮件地址。')]")
