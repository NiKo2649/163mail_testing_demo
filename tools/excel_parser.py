# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/24 0:48
# @Author : NiKo
# @File : excel_parser.py
# @Software: PyCharm

import openpyxl

class ExcelParser(object):
    def __init__(self, file_path):
        self.workbook = openpyxl.load_workbook(file_path)

