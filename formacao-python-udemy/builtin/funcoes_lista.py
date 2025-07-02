lista = [5,10,2,1,5]
lista.sort() # Ordernando lista
print(lista)

lista = ["a","b","x","ab","d","c"]
lista.sort(reverse=True) # Ordenando lista decrescente
print(lista)

def sort_por_tamanho(item): # Criando função para odernar pelo tamanho das strings
    return len(item)

lista = ["a","b","ab","de","abc","abcd"]
lista.sort(key=sort_por_tamanho) # Passando chave para ordenar por tamanho.
print(lista)

lista = [5,10,2,1,5]
lista.reverse() # Inverter lista
print(lista)

produtos = [
    ["carro", "R$ 100.000"],
    ["cadeira","R$ 1000"],
    ["moto", "R$ 40.000"],
    ["geladeira", "R$ 2000"],
    ["armario","R$ 1500"]
]

for produto, valor in produtos:
    print(produto,valor)

nomes = ('José','Carlos','João')
dicionario = dict.fromkeys(nomes,10) # Atribuindo cada valor para uma chave no dicionário
print(dicionario)