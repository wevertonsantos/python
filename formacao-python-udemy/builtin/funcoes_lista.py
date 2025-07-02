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