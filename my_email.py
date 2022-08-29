from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender="frimpsup@gmail.com"
email_password=password

email_receiver="PUT HERE YOUR RECEIVER'S ADDRESS"
subject='Send me my money'
body=""""
when i get u for campus it will be bloody if u dont want any case send my money fast and be secured
"""
em=EmailMessage()
em['from']=email_sender
em['to']=email_receiver
em['subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver,em.as_string())
