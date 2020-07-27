# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 16:15
# @Author : NiKo
# @File : conftest.py
# @Software: PyCharm

import pytest
from selenium import webdriver

_driver = None


@pytest.fixture(scope='module')
def driver():
    global _driver
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    _driver.quit()
