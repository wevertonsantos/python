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

# Usando operações com o x da lista
lista = [x*2 for x in range(-10,21) if x <= 10 if x >= 0]
print(lista)

lista = [str(x) for x in range(-10,21) if x <= 10 if x >= 0]
print(lista)

lista = ['negativo' if x < 0 else 'positivo' for x in range(-3,4)]
print(lista)

lista = [str(x) + ' par' if x % 2 == 0 else str(x) + ' impar' for x in range(2,11)]
print(lista)

lista = [1,2,3,4,5,6,7,8,9]
lista = list(filter(lambda x: x % 2 == 0, lista))
print(lista)

lista = [[str(x) + str(y) for x in range(1,5)] for y in range(1,5)]