# 06/07/2020
''' This project is going to send me the weather via email or text.'''

import smtplib
import os 
import ssl

port = 465

sender = 'ejpythonbot123@gmail.com'

password = 'Sonofgina1'

recieve = 'son_of_gina@yahoo.com'

message = """\
Subject: Python Email Tutorial

This is from python!

Ej test bot """

print('Starting to send')
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)

print('sent email')