import requests
from time import gmtime, strftime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

from utils import find_resource

resource = {
    "label": "Equipments"
}

component = {
    "label": "Mouse", 
} 

tag = {
    "label": "Computers"
}

# Get resource
found = find_resource(resource["label"])

# Create component
component["resource"] = found["uuid"]


r = requests.post("%s/components" % (get_api_endpoint(),), headers={'Authorization': 'Bearer ' + get_token()}, json=component)
component = r.json()

# Create tag
r = requests.post("%s/componentTags" % (get_api_endpoint(),), headers={'Authorization': 'Bearer ' + get_token()}, json=tag)
tag = r.json()


# Link Both
r = requests.patch("%s/components/%s" % (get_api_endpoint(), component["uuid"]), headers={'Authorization': 'Bearer ' + get_token()}, json={"tags": [tag["uuid"]]})






