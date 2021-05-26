import requests

p={"page":2}
#resp = requests.get("https://reqres.in/api/users?page=2")--without params
resp = requests.get("https://reqres.in/api/users", params=p)

print(resp)
code = resp.status_code
assert code==200 ,"code doesn't match"
print(resp.content)
print(resp.text)
print(resp.json())
print(resp.headers)
print(type(resp.headers))
print(resp.cookies)
print(resp.encoding)
print(resp.url)
json_resp = resp.json()
print(json_resp["total_pages"])
print(json_resp["total"])
print(json_resp["data"][0]["email"])
assert (json_resp["data"][0]["email"]).endswith("reqres.in"), "email format not matching"
print(json_resp["data"][3]["first_name"])
assert (json_resp["data"][3]["first_name"]) != None
print(json_resp["support"]["url"])