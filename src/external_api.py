import requests
from utils import json_data

def converter_value():
  to = 'RUB'
  fromm = 'USD'
  for dict_data in json_data():
    if dict_data.get("operationAmount",{}).get("currency",{}).get("code") == 'USD':
      amount = dict_data.get("operationAmount", {}).get('amount')
      url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={fromm}&amount={amount}"
      payload = {}
      headers= {
        "apikey": "FJ3E7A57QzroJzYxRO1CGs7xrUELYDNM"
        }
      response = requests.request("GET", url, headers=headers, data = payload)
      status_code = response.status_code
      result = response.text
      return dict(result).get('query',{}).get('amount')

print(converter_value())
def return_sum_transaction():
  for dict_data in json_data():
    if dict_data.get("operationAmount",{}).get("currency",{}).get("code") == 'RUB':
      print(dict_data['operationAmount']['amount'])

print(return_sum_transaction())