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