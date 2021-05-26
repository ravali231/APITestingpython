import requests
import json
import identity1

def __init__(self):
    self.ctk_token = identity1.fetch_token()
    print(self.ctk_token)

"""
url = "https://staging.identity-internal.api.rackspacecloud.com/v2.0/tokens"
mydata = open("data1.json", "r").read()
print(mydata)
request_json = json.loads(mydata)
print(request_json)
resp = requests.post(url, data=request_json, verify=False)
print(resp)
print(resp.json())
"""




# response = requests.request("POST", sync_requests, data=json.dumps(payload), headers=headers, verify=False)
# request_json = json.dumps(mydata)

"""iteration code with for loop
    for i in range(len(inbound_dict)):
        for j in range(i + 1, len(inbound_dict)):
            if inbound_dict[i] > inbound_dict[j]:
                print("exceed")#exceed is printing 50 times first and then decreasing.
                #print("inbound dict i is greater than j")
        print(inbound_dict[i])"""