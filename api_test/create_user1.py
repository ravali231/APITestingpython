import json

import requests

mydata = open("data.json","r").read()

resp = requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['job']=="Automation","job doesn't match"
