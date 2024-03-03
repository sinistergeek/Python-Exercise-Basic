import json
import requests
from pprint import pprint

url = "https://company.clearbit.com/v1domains/find?"

params = {
        'name':'Educative'
        }
headers = {
        'Content-Type' : 'application/json',
        'Authorization': 'Bearer {{API_KEY}}'
        }

response = requests.request("GET",url,headers=headers,params=params)
