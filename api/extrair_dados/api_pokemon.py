import requests,json # importando requests para fazer requisição

url = "https://pokeapi.co/api/v2/pokemon/" # passando url

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).text # retornando o conteúdo com .text do response

print(response.text)