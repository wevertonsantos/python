import requests,json # importando requests para fazer requisição

url = "https://pokeapi.co/api/v2/pokemon/" # passando url

payload = {}
headers = {}

response = json.loads(requests.request("GET", url, headers=headers, data=payload).text) # transformando retorno o request em json

for item_pokemon in response['results']: # acessando cada registro que retorna lista do results
    print(item_pokemon)