import json
import requests
from pprint import pprint

url = "https://person.clearbit.com/v2/people/find?"

params = {
        'email':'{{EMAIL}}'
        }

headers = {
        'Content-Type':'application/json',
        'Authorization':'Bearer {{API_KEY}}'
        }

response = requests.request("GET",url,headers=headers,params=params)
print(json.dumps(response.json(),indent=4))

