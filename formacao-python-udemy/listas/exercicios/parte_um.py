# 1 - Crie uma lista com os seguintes números 1,10,6,7,8,10. Em seguida printe a soma destes números.

lista = [1,10,6,7,8,10]
total = 0
for num in lista:
    total += num
print("Soma dos números:",total)

# 2 - Cria uma lista e preencha ela com valores de 1 a 100. Em seguida printe esses valores.

lista = []
lista += range(1,101)
print(lista)

'''
3 - Crie duas listas com os seguintes valores 30,4,43,52,65,-10 e 
# 43,2,4,76,32,65,3. Agora faça a junção dessas listas, mas se houverem valores repetidos entre ambas eles não podem repetir na lista unida.
'''

lista_um = {30,4,43,52,65,-10}
lista_dois = {43,2,4,76,32,65,3}
sets_uniao = lista_um.union(lista_dois)
print(sets_uniao)