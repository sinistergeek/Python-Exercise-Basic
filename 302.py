import configparser
import os
import requests

def shorten(url):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),'api.cfg'))

    query_params = { 'access_token': bittly_config['bitly']['access_token'],'longUrl' : uri}
    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params = query_params,verify = False)

    data = response.json()

    if not data['status_code'] == 200:
        exit("Unexpected status_code: {} in bitly resonse. {}".format(data['status_code'],response.text))
        return data['data']['url']
print(shorten('http://code-maven.com'))
