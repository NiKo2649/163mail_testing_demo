# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/24 0:48
# @Author : NiKo
# @File : config_parser.py
# @Software: PyCharm

import configparser

class ConfigParser(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("../config.ini", encoding='utf-8')

    def get_section(self, section):
        try:
            data = self.config.options(section)
            return data
        except configparser.NoSectionError as e:
            print()

    def get_option(self, section, option):
        try:
            data = self.config.get(section, option)
            return data
        except configparser.NoOptionError as e:
            print()


if __name__ == '__main__':
    Config = ConfigParser()
    data = Config.get_section('base')
    print(data)
    for item in data:
        print(Config.get_option('base', item))
