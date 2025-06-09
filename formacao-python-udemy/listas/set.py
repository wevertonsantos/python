# Declaração set:
set = {}
set = {1,2,3}
#print(set[0]) # Não podemos olhar determinada posição
#set[0] = 1 # Não pode alterar valores
set.add(5) # Adicionando elemento
set.remove(1) # Removendo valores
set = {1,2,2} # Ele não permite duplicidade
set.clear() # Remove todos os elementos

set = {1,2,3,4,5,5.6,False}
for item in set: #interação apenas com itens
    print(item)
sett = {7,8}
sets = set.union(sett) # União de sets
print(sets)