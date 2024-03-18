import requests

from api import get_token, get_api_endpoint



def find_resource(label):
    # Get resources
    more = True
    page = 1
    found = None

    while more:
        r = requests.get("%s/resources?page=%s" % (get_api_endpoint(), page), headers={'Authorization': 'Bearer ' + get_token()})
        res = r.json()

        for resource in res["items"]:
            if resource["label"]==label:
                found = resource
                break

        if found is not None:
            more = False
        else:
            if res["pager"]["pageSize"]<=len(res["items"]):
                page += 1
            else:
                more = False

    return found


def find_component(label):
    # Get resources
    more = True
    page = 1
    found = None

    while more:
        r = requests.get("%s/components?page=%s" % (get_api_endpoint(), page), headers={'Authorization': 'Bearer ' + get_token()})
        res = r.json()

        for resource in res["items"]:
            if resource["label"]==label:
                found = resource
                break

        if found is not None:
            more = False
        else:
            if res["pager"]["pageSize"]<=len(res["items"]):
                page += 1
            else:
                more = False

    return found


def get_users(fields, attributes):
    """
    Retrieve list of users with firstname == philippe
    """

    url = '%s/users?fields=%s&%s' %  (get_api_endpoint(), fields, "&".join(
            [
                "attribute.%s=%s:%s" % (param['attribute'], param['operator'], param['value']) for param in attributes
            ]
        ))


    r = requests.get(
        url,
        headers={'Authorization': 'Bearer ' + get_token()}
    )

    return r.json()["items"]
