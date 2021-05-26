import requests
import json

from api_test import identity3

def test_comparecreateddate():
    access_token = identity3.fetch_Token()

    url = "https://api-interactions-api-staging.devapps.rsi.rackspace.net/v1/interactions?offset=0&count=50&sort=created_at&sort_order=asc&created_at_lt=2016-04-08T01:20:23.142Z"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    resp = requests.get(url,headers=headers)
    resp_json = resp.json()
    inbound_dict = []
    for item in resp_json['interactions']:
        created_id = item['created_at']
        #print(created_id)
        if created_id not in inbound_dict:
            inbound_dict.append(created_id)

    print(inbound_dict)
    count = len(inbound_dict)
    print(count)
    i=0
    j=1
    while(i<len(inbound_dict) and j<len(inbound_dict)):
        print(inbound_dict[i], inbound_dict[j])
        if (inbound_dict[i])<(inbound_dict[j]):
            print(inbound_dict[i])
        else:
            print(inbound_dict[i] +" is greater than "+ inbound_dict[j])

        i +=1
        j +=1

    print("compared created and updated dates")

"""
test_comparecreateddate()

def test_createsupportedinter():
    access_token = identity3.fetch_Token()

    url = "https://api-interactions-api-staging.devapps.rsi.rackspace.net/v1/interactions"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    data = open("data2.json", "r").read()
    json_request = json.loads(data)

    resp = requests.post(url, headers=headers, json=json_request)
    resp_json = resp.json()

    print(resp_json)
    print(resp.status_code)
    print(resp_json['id'])
    print(resp_json['template_id'])

test_createsupportedinter()


def test_createunsupportedinter():
    access_token = identity3.fetch_Token()

    url = "https://api-interactions-api-staging.devapps.rsi.rackspace.net/v1/interactions"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    data = open("data3.json", "r").read()
    json_request = json.loads(data)

    resp = requests.post(url, headers=headers, json=json_request)
    resp_json = resp.json()

    print(resp_json)
    print(resp.status_code)
    print(resp_json['id'])
    print(resp_json['template_id'])

test_createunsupportedinter()


def test_comparecrtdtaccts():
    access_token = identity3.fetch_Token()

    url = "https://api-interactions-api-staging.devapps.rsi.rackspace.net/v1/interactions/accounts/CLOUD/323676?sort=created_at&sort_order=desc&offset=0&count=50"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    resp = requests.get(url,headers=headers)
    resp_json = resp.json()
    inbound_dict = []
    for item in resp_json['interactions']:
        created_id = item['created_at']
        #print(created_id)
        if created_id not in inbound_dict:
            inbound_dict.append(created_id)

    print(inbound_dict)
    count = len(inbound_dict)
    print(count)
    i=0
    j=1
    while(i<len(inbound_dict) and j<len(inbound_dict)):
        print(inbound_dict[i], inbound_dict[j])
        if (inbound_dict[i])<(inbound_dict[j]):
            print(inbound_dict[i])
        else:
            print(inbound_dict[i] +" is greater than "+ inbound_dict[j])

        i +=1
        j +=1

    print("compared created and updated dates")

test_comparecrtdtaccts()
"""