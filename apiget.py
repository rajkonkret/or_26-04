# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/

import requests as re

# pip install requests

response = re.get('http://api.nbp.pl/api/exchangerates/rates/A/EUR/')
print(response)

# 2... - ok
# 3 ...
# 4.. bład, bład zapytania, z lub 404 zasob nie istnieje
# 5 .. wewnetrne błedy serwera
table = response.json()
print(table)
# wypisac 'mid'
print(table['rates'])
print(table['rates'][0])
print(table['rates'][0]['mid'])