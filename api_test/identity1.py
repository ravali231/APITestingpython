import os
import requests

url = 'https://staging.identity-internal.api.rackspacecloud.com/v2.0/tokens'

data = {

    'auth':
        {
        'RAX-AUTH:domain':
            {
            'name': 'Rackspace'
            },
            'passwordCredentials':
            {
                'username': 'rava5622',
                'password': 'Edhere@123'
            }
        }
    }

r = requests.post(url, json=data)
#print(r.json())
print(r.json()['access']['token']['id'])


"""def fetch_token():
    data = {

        'auth':
            {
                'RAX-AUTH:domain':
                    {
                        'name': 'Rackspace'
                    },
                'passwordCredentials':
                    {
                        'username': 'rava5622',
                        'password': 'Edhere@123'
                    }
            }
    }

    r = requests.post(url, json=data)
    print(r.json())
    return r.json()['access']['token']['id']
    """