import json
import os
import requests


def fetch_Token():
    url = 'https://staging.identity-internal.api.rackspacecloud.com/v2.0/tokens'
    data = open("data1.json","r").read()
    json_request = json.loads(data)
    #print(json_request)

    r = requests.post(url, json=json_request)
    #print(json.dumps(r.json()))
    #print(r.json())
    #print(r.json()['access']['token']['id'])
    return r.json()['access']['token']['id']

fetch_Token()

