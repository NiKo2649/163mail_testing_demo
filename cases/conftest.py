# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 16:15
# @Author : NiKo
# @File : conftest.py
# @Software: PyCharm

import pytest

from page.login_page import LoginPage
from page.contact_page import ContactPage
from tools.config_parser import ConfigParser
from tools.excel_parser import ExcelParser

p = ConfigParser("config.ini")
userName = p.get("base", "test_account")
passWord = p.get("base", "test_password")


@pytest.fixture(scope='class')
def init_login_pages(driver):
    login_page = LoginPage(driver)
    login_page.open_url()
    yield login_page


@pytest.fixture(scope='function')
def open_url(init_login_pages):
    login_page = init_login_pages
    yield login_page
    login_page.del_cookies()
    login_page.refresh()


@pytest.fixture(scope='class')
def had_login(init_login_pages):
    login_page = init_login_pages
    login_page.login(userName, passWord)
    contact_page = ContactPage(login_page.driver)
    yield contact_page
    login_page.del_cookies


@pytest.fixture(scope='function')
def refresh_page(had_login):

    yield
    had_login.refresh()
