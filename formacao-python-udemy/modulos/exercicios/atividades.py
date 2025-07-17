# 1 - Importe do modulo random a função randrange e crie um programa que gere 
# um único número aleatório entre 2 e 100. Em seguida diga se esse número é 
# par ou impar.

from random import randrange

numero_aleatorio = randrange(2,100)

if numero_aleatorio % 2 == 0:
    print(numero_aleatorio, "Número par")
else:
    print(numero_aleatorio, "Número ímpar")

# 2 - Da mesma forma que o exercício anterior, gere a soma de 100 números 
# aleatórios e mostre o resultado final.

i = 0
soma = 0
while i <= 100:
    soma += randrange(1,100)
    i += 1

print(soma)

# 3 - Crie um modulo que dispõem de duas funções, uma que subtrai dois números 
# e outra que soma dois números. Importe essas funções e as use. 
# Não se esqueça de gerar a documentação destas funções e do modulo e mostrar 
# na saída de seu programa. Chame o modulo de “calc_python”

import calc_python

print(calc_python.soma.__doc__)
calc_python.soma(10,20)
print(calc_python.subtracao.__doc__)
calc_python.subtracao(20,10)

# 4 - Cria um modulo para retornar uma lista de números aleatórios. 
# Esse modulo deve ter a seguinte funcionalidade:
# - Uma função que retorna uma lista de números randômicos chamada de 
# get_random_lista(inicial, final, tam), onde “inicial” é o número mínimo 
# que pode aparecer na lista e “final” é o número máximo que pode aparecer. 
# Por fim “tam” deve ser o número de elementos na lista. 
# Chame o modulo de “meu_random”