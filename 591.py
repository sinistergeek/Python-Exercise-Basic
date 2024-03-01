import requests
import json

url = "https://api.sandbox.transferwise.tech/v1/accounts"

payload = json.dumps({
    "accountHolderName": "Educative by API",
    "currency": "GBP",
    "type": "sort_code",
    "details": {
        "legalType": "PRIVATE",
        "sortCode": "231470",
        "accountNumber": "28821922",
        "email": "example@gmail.com"
    }
})
headers = {
    'Authorization': 'Bearer {{token}}',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(json.dumps(response.json(), indent=4))
