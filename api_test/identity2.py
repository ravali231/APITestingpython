import json
import os
import requests


def test_fetchToken():
    url = 'https://staging.identity-internal.api.rackspacecloud.com/v2.0/tokens'
    data = {
        'auth': {
            'RAX-AUTH:domain': {
                'name': 'Rackspace'
            },
            'passwordCredentials': {
                'username': 'rava5622',
                'password': 'Edhere@123'
            }
        }
    }

    r = requests.post(url, json=data)
    #print(json.dumps(r.json()))
    print(r.json())
    print(r.json()['access']['token']['id'])

test_fetchToken()
