import requests

from config import *

def get_api_endpoint():
    return "https://%s/%s" % (API_SERVER, API_VERSION)
    

def get_token():
    """
        Get an access token
    """

    r = requests.post(
        API_TOKEN, 
        data={
            'client_id': API_CLIENT_ID,
            'client_secret': API_CLIENT_SECRET,
            'grant_type': 'client_credentials',
            'scope': '2jJO5LQz',
        })

    data = r.json()
    token = data['access_token']

    return token
