import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from emailer.email_service import EmailService



class GmailService(EmailService):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

        self.server = smtplib.SMTP("smtp.gmail.com", 587)

        try:
            self.server.ehlo()
            self.server.starttls()
            self.server.login(username, password)
        except smtplib.SMTPHeloError as exception:
            print(exception)

    def send_email(self, recipient: str, subject: str, body: str):
        msg = MIMEMultipart()
        
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body.encode('utf-8'), _charset='utf-8'))

        self.server.sendmail("Friendmas Kris Kringle Bot", recipient, msg.as_string())

    def close_email_server(self):
        self.server.close()
