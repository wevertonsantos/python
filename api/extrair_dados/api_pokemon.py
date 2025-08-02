import requests,json # importando requests para fazer requisição

url = "https://pokeapi.co/api/v2/pokemon/" # passando url

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload) # retornando a requisição com método get e passando a url

print(response.text)