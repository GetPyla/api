import requests
from api import get_token, get_api_endpoint

from utils import find_component, get_users

# Fields we want to retrive
fields = "firstname,lastname,email,startDate,lifecycle,uuid"

attributes = [
    {
        'attribute': 'email',
        'operator': 'eq',
        'value': 'philippe@getpyla.com'
    }
]


component = {
  "label": "PC"
}

found = find_component(component["label"])

users = get_users(fields, attributes)

user = users[0]

print(user)
print(found)

r = requests.post('%s/users/%s/components' %  (get_api_endpoint(), user["uuid"]), json={})


