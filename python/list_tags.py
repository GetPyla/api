import requests
from time import gmtime, strftime

from api import get_token, get_api_endpoint
from config import *

listing = []
page = 1

while True:
    r = requests.get("%s/componentTags?page=%s" % (get_api_endpoint(), page), headers={'Authorization': 'Bearer ' + get_token()})
    listing_page = r.json()

    listing = [*listing, *listing_page["items"]]

    if len(listing)==listing_page["pager"]["total"]:
        break
    else:
        page += 1

print("LENGTH: ", len(listing))
print(listing)

    





