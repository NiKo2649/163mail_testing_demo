# venv/Scripts/
# -*- coding: utf-8 -*-
# @Time : 2020/7/27 15:58
# @Author : NiKo
# @File : send_mail.py
# @Software: PyCharm
import yagmail
from tools.config_parser import ConfigParser

p = ConfigParser("../config.ini")
s = "auto_send_mail_setting"

class SendMail(object):

    @staticmethod
    def send_mail(to_user, subject, contents, file):
        mail = yagmail.SMTP(p.get(s, "sender_mail"), p.get(s, "sender_password"), p.get(s, "smtp_server"))
        mail.send(to_user, subject, contents, file)


if __name__ == '__main__':
    SendMail.send_mail('smtp.163.com',
                                 '13417072649@163.com',
                                 'CLAOIRSRINBXPYRZ',
                                 '330908191@qq.com',
                                 'python自动化测试',
                                 '邮件正文',
                                 '../test.py')
