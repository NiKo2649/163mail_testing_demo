# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 0:48
# @Author : NiKo
# @File : config_parser.py
# @Software: PyCharm

import configparser


class ConfigParser(object):
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file, encoding='utf-8')

    def get_section(self, section):
        try:
            data = self.config.options(section)
            return data
        except configparser.NoSectionError as e:
            print()

    def get(self, section, option):
        try:
            data = self.config.get(section, option)
            return data
        except configparser.NoOptionError as e:
            print()


