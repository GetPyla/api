import requests
from time import gmtime, strftime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

from utils import find_resource

new_resource = {
    "label": "Equipments", 
} 

found = find_resource(new_resource["label"])


if not found:
    r = requests.post("%s/resources" % (get_api_endpoint(),), headers={'Authorization': 'Bearer ' + get_token()}, json=new_resource)
    print(r.text)



