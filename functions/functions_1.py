#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(message):
    msg = MIMEText(message,'plain','utf-8')
    msg['From'] = formataddr(["Tony","it.s@x-tl.com.cn"])
    msg['To'] = formataddr(['爱在七元钱','154293106@qq.com'])
    msg['Subject'] = "鑫泰利报警系统"

    server = smtplib.SMTP("smtp.x-tl.com.cn",25)
    server.login("it.s","19840807hxc!")
    server.sendmail('it.s@x-tl.com.cn',['154293106@qq.com',],msg.as_string())
    server.quit()

