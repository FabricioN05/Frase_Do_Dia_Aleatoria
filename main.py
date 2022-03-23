import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

class EmailObject:
    def __init__(self, subject, _from, to, html):
        self._message = MIMEMultipart()
        self._message["Subject"] = subject
        self._message["From"] = _from
        self._message["To"] = to
        self._message.attach(MIMEText(html, 'html'))

    @property
    def message(self):
        return self._message.as_string()

    @message.setter
    def message(self, parte, modificacao):
        self._message[parte] = modificacao


def send_email(emails, subject, my_email, my_password, html):
    if type(emails) == "str":
        emails = [emails]
    elif type(emails) == 'int':
        return TypeError('O email não pode ser do tipo (int)')

    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(my_email, my_password)
        for email in emails:
            email_object = EmailObject(subject, my_email, email, html)
            server.sendmail(my_password, email, email_object.message)
            
