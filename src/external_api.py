import requests

amount = 845
fromm = 'RUB'
to = 'EUR'
url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={fromm}&amount={amount}"

payload = {}
headers= {
  "apikey": "FJ3E7A57QzroJzYxRO1CGs7xrUELYDNM"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)