import requests
from time import gmtime, strftime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

from utils import find_resource

resource = {
    "label": "Equipments", 
} 


component = {
  "label": "PC"
}


found = find_resource(resource["label"])

if found is not None:
    component["resource"] = found["uuid"]
    r = requests.post("%s/components" % (get_api_endpoint(),), headers={'Authorization': 'Bearer ' + get_token()}, json=component)
    print(r.text)



