import requests

url = 'https://api.bithumb.com/public/ticker/BTC_KRW'
headers = {'prev_closing_price' : 'application/json'}
response = requests.get(url)

print(response.json()['data']['prev_closing_price'])