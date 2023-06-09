import requests
from time import gmtime, strftime
import datetime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

# In five days
in_five_days = (datetime.datetime.now()+datetime.timedelta(20)).strftime("%Y-%m-%d")


# Fields we want to retrive
fields = "firstname,lastname,email,startDate,lifecycle"

# Lifecycle values
lifecycles = "in:CREATED,PREONBOARDING"


def get_users():
    """
    Retrieve list of users who arrives in 5 days
    """
    r = requests.get(
        '%s/users?fields=%s&startDate=eq:%s' % (get_api_endpoint(), fields, in_five_days), 
        headers={'Authorization': 'Bearer ' + get_token()})

    return r.json()["items"]


## Users
users = get_users()

## Subject for the mail
subject = "Users who arrives in 5 days"

## Text version
text = """
Here are users who arrives in 5 days:
%s
""" % ("\n".join(["%s %s" % (user["firstname"], user["lastname"]) for user in users]))

## Sending email
send_email(EMAIL_SMTP_RECIPIENT, subject, text)


