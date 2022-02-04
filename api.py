import requests
from requests.api import request 

req = requests.get('https://economia.awesomeapi.com.br/json/last/:moedas')
#req = request.json()
print(req) 
