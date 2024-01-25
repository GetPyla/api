import requests

from api import get_token, get_api_endpoint
from config import *

# Fields we want to retrive
fields = "firstname,lastname,email,startDate,lifecycle"

attributes = [
    {
        'attribute': 'firstname',
        'operator': 'eq',
        'value': 'Philippe'
    }
]


def get_users():
    """
    Retrieve list of users with firstname == philippe
    """

    url = '%s/users?fields=%s&%s' %  (get_api_endpoint(), fields, "&".join(
            [
                "attribute.%s=%s:%s" % (param['attribute'], param['operator'], param['value']) for param in attributes
            ]
        ))
    
    print(url)

    r = requests.get(
        url,
        headers={'Authorization': 'Bearer ' + get_token()}
    )

    return r.json()["items"]


## Users
users = get_users()

for user in users:
    print(user)




