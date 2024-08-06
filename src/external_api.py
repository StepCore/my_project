import requests
import json
from utils import json_data

list_transaction = []
def converter_value():
    list_converted = []
    for summ in list_transaction:
        if 'USD' in summ:
            amount = summ[:-4]
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            payload = {}
            headers = {
              "apikey": "jqhlspps8Cks9V3f4XwGI5qZrXx5gcpj"
              }
            response = requests.request("GET", url, headers=headers, data = payload)
            status_code = response.status_code
            result = json.loads(response.text)
            list_transaction[list_transaction.index(summ)] = result['result']
    return list_transaction


def return_sum_transaction():
    for dict_data in json_data():
        if dict_data.get("operationAmount",{}).get("currency",{}).get("code") == 'RUB':
            list_transaction.append(dict_data['operationAmount']['amount'])
        elif dict_data.get("operationAmount", {}).get("currency", {}).get("code") == 'USD':
            list_transaction.append(dict_data['operationAmount']['amount'] + ' ' + 'USD')
    return list_transaction


return_sum_transaction()
converter_value()

print(*list_transaction, sep='\n')