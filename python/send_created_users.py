import requests
from time import gmtime, strftime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

# Today's date
today = strftime("%Y-%m-%d", gmtime())

# Fields we want to retrive
fields = "firstname,lastname,email,startDate,lifecycle"

# Lifecycle values
lifecycles = "in:CREATED,PREONBOARDING"


def get_users():
    """
    Retrieve list of users that are not onboarded yet (CREATED and PREONBOARDING lifecycles) and where start date is in the future
    """
    r = requests.get(
        '%s/users?fields=%s&lifecycle=%s&startDate=gt:%s' % (get_api_endpoint(), fields, lifecycles, today), 
        headers={'Authorization': 'Bearer ' + get_token()})

    return r.json()["items"]


## Users
users = get_users()

## Subject for the mail
subject = "Non onboarded users"

## Text version
text = """
Here are users that are not onboarded yet:
%s
""" % ("\n".join(["%s %s" % (user["firstname"], user["lastname"]) for user in users]))

## Sending email
send_email(EMAIL_SMTP_RECIPIENT, subject, text)



