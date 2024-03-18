import requests
from time import gmtime, strftime

from api import get_token, get_api_endpoint
from config import *


tag = {
    "label": "Computers"
}


r = requests.post("%s/componentTags" % (get_api_endpoint(),), headers={'Authorization': 'Bearer ' + get_token()}, json=tag)
print(r.text)



