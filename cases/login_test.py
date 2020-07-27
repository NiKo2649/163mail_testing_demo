# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 16:14
# @Author : NiKo
# @File : login_test.py
# @Software: PyCharm
import pytest
from tools.excel_parser import ExcelParser
e = ExcelParser()
sheet =e.get_all_values_of_sheet(e.get_sheet_by_name("login"))


class TestLogin(object):

    @pytest.mark.parametrize('username, password', [sheet[0]])
    @pytest.mark.xfail()
    def test_login_fail_by_mistake_password(self, init_login_pages, open_url, username, password):
        login_page = init_login_pages
        login_page.login(username, password)
        assert login_page.is_login_failed()

    @pytest.mark.parametrize('username, password', [sheet[1]])
    def test_login_succeed(self, init_login_pages, open_url, username, password):
        login_page = init_login_pages
        login_page.login(username, password)
        assert login_page.is_login_succeed
