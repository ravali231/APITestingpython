import requests
import json

from api_test import identity3

def test_comparedate():
    access_token = identity3.fetch_Token()
    print(access_token)

    url = "https://api-interactions-api-staging.devapps.rsi.rackspace.net/v1/interactions?sort_order=desc&offset=0&count=50&updated_at_lt=2021-04-16T18:10:22.059Z&sort=created_at"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': access_token,
        'Accept': "application/json"
    }
    resp = requests.get(url,headers=headers)
    #print(resp.json())
    i=0;
    #created_at = (resp.json()["interactions"][i]["created_at"])
    while(i<50):
        created_at = (resp.json()["interactions"][i]["created_at"])
        updated_at = (resp.json()["interactions"][i]["updated_at"])
        print(created_at)
        print(updated_at)
        if (created_at == updated_at):
            print("created_at and updated_at values matched")
        else:
            print("created_at and updated_at values doesn't match")
        i += 1
    date_count = i
    print("Total Date Count is " +str(date_count))
    print("compared created and updated dates")


test_comparedate()



