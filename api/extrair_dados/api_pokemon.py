import requests,json # importando requests para fazer requisição

url = "https://pokeapi.co/api/v2/pokemon/" # passando url
pokemon_list = []

while url != None:
    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text) # transformando retorno o request em json

    url = response['next'] # url da próxima página

    for item_pokemon in response['results']: # acessando cada registro que retorna lista do results
        pokemon_name = item_pokemon['name']
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}" # pegando cada pokemon com sua devida url
        response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text) # retorno da url de cada pokemon

        infos = { # criando dic para ter informações básicas de cada pokemon
            "name":pokemon_name,
            "id":response_pokemon["id"],
            "height":response_pokemon["height"],
            "weight":response_pokemon["weight"],
            "is_default":response_pokemon["is_default"]
        }

        pokemon_list.append(infos)

print(pokemon_list) # printando lista de todos os pokemons