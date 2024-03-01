import requests

url = "https://www.uuidgenerator.net/api/guid"

response = requests.request("GET", url)

print(response.text)
