import requests
from time import gmtime, strftime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

# Today's date
today = strftime("%Y-%m-%d", gmtime())

# Fields we want to retrive
fields = "firstname,lastname,email,startDate,lifecycle,manager"

# Lifecycle values
lifecycles = "PREONBOARDING"


def get_users():
    """
    Retrieve list of users that are not onboarded yet (PREONBOARDING lifecycles) and where start date is in the future
    """
    r = requests.get(
        '%s/users?fields=%s&lifecycle=%s&startDate=gt:%s' % (get_api_endpoint(), fields, lifecycles, today), 
        headers={'Authorization': 'Bearer ' + get_token()})

    return r.json()["items"]

def get_user(uuid):
    """
    Retrieve a user
    """
    r = requests.get(
        '%s/users/%s?fields=%s' % (get_api_endpoint(), uuid, fields), 
        headers={'Authorization': 'Bearer ' + get_token()})

    return r.json()


## Users
users = get_users()

## Must group users by manager
users_by_manager = {}

for user in users:
    users_by_manager.setdefault(user["manager"], [])
    users_by_manager[user["manager"]].append(user)

for manager_uuid in users_by_manager.keys():

    if manager_uuid is not None:
        manager = get_user(manager_uuid)
        

        # ## Subject for the mail
        subject = "Non onboarded users"

        ## Text version
        text = """
        Here are users that are not onboarded yet:
        %s
        """ % ("\n".join(["%s %s" % (user["firstname"], user["lastname"]) for user in users_by_manager[manager_uuid]]))

        ## Sending email
        send_email(manager["email"], subject, text)







