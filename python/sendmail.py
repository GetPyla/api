import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import *


def send_email(recipient, subject, text, html=None):

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = EMAIL_SMTP_SENDER
    message["To"] = recipient


    # Turn these into plain/html MIMEText objects
    parts = [MIMEText(text, "plain")]

    if html is not None:
        parts.append(MIMEText(html, "html"))

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    for part in parts:
        message.attach(part)
    

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT, context=context) as server:
        server.login(EMAIL_SMTP_SENDER, EMAIL_SMTP_PASSWORD)
        server.sendmail(
            EMAIL_SMTP_SENDER, message["To"], message.as_string()
        )



   
