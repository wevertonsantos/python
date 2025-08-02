import requests,json # importando requests para fazer requisição

url = "https://pokeapi.co/api/v2/pokemon/" # passando url

while url != None:
    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text) # transformando retorno o request em json

    url = response['next'] # url da próxima página

    for item_pokemon in response['results']: # acessando cada registro que retorna lista do results
        pokemon_name = item_pokemon['name']
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}" # pegando cada pokemon com sua devida url
        response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text) # retorno da url de cada pokemon