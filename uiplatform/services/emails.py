# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         emails.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------

import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

from config import Config


def send_email_reports(receiver, html_report_path):

    if '@sina.com' in Config.EMAIL_SENDER:
        smtp_server = 'smtp.sina.com'
    elif '@163.com' in Config.EMAIL_SENDER:
        smtp_server = 'smtp.163.com'
    else:
        smtp_server = 'smtp.exmail.qq.com'

    subject = "UI自动化测试报告"

    with io.open(html_report_path, 'r', encoding='utf-8') as stream:
        send_file = stream.read()

    att = MIMEText(send_file, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = TestReports.html"

    body = MIMEText("附件为定时任务生成的接口测试报告，请查收，谢谢！", _subtype='html', _charset='gb2312')

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['from'] = Config.EMAIL_SENDER
    msg['to'] = receiver
    msg.attach(att)
    msg.attach(body)

    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.starttls()
    smtp.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)
    smtp.sendmail(Config.EMAIL_SENDER, receiver.split(','), msg.as_string())
    smtp.quit()



