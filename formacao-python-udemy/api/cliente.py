import requests

x = requests.get('http://127.0.0.1:5000/cotacao/') # pegando cotacao com método get
print(x.text)

x = requests.get('http://127.0.0.1:5000/') # pegando cotacao com método get
print(x.text)

x = requests.get('http://127.0.0.1:5000/conversao/100.0')
print(x.text)

x = requests.get('http://127.0.0.1:5000/cotacaocompleta?valor=100&mes=Marco')
print(x.text)

x = requests.get('http://127.0.0.1:5000/tabela/')
print(x.text)