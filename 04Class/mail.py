# -*- coding: utf-8 -*-
import smtplib

from email.mime.text import MIMEText

SMTPServer = "smtp.163.com"
sender = "zhangjian_linux@163.com"
passwd = "Zhangjian520"

message = "zhang jian is a good man"
msg = MIMEText(message)

msg["Subject"] = "Zhang.Jayce"
msg["From"] = sender

mailServer = smtplib.SMTP(SMTPServer, 25)
mailServer.login(sender, passwd)

mailServer.sendmail(sender, ["zhangjian3032@gmail.com", "zhangjian_linux@163.com"], msg.as_string())

mailServer.quit()

print(msg)
