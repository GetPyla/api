import requests
from time import gmtime, strftime

from sendmail import send_email
from api import get_token, get_api_endpoint
from config import *

new_user = {
    "firstname": "John", 
    "lastname": "Doe",
    "email": "john_doe@exemple.org"
} 

r = requests.post("%s/users?fields=uuid,email,firstname,lastname" % (get_api_endpoint()), headers={'Authorization': 'Bearer ' + get_token()}, json=new_user)
print(r.text)



