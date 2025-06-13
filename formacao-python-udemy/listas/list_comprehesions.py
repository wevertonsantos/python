# Declaração de uma lista comprehension
lista = [x for x in range(0,10)]
print(lista)

# Percorrendo lista
lista = ['zero','um','três']
lista = [x for x in lista]
print(lista)

# Usando lista comprehension com if
lista = [x for x in range(1,11) if x % 2 == 0]
print(lista)

# Usando lista comprehension com mais de uma condição lógica
lista = [x for x in range(-10,21) if x <= 10 if x >= 0]
print(lista)