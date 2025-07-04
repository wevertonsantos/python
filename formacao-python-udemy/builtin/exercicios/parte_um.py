# 1 - Crie uma função que retorne a subtração de dois elementos, mas que considere o valor absoluto deste valores.

def subtracao(x,y):
    return (abs(x) - abs(y))

print(subtracao(-10,5))

"""
2 – Sem usar “ifs”, crie uma função que receba dois números e retorne a soma 
dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser 
sempre maior que 0.
"""

def soma(x,y):
    soma = x + y
    soma = min(10000,soma)
    soma = max(0,soma)
    return soma

"""
3 - Crie uma função que receba argumentos de tamanho arbitrário. 
Todos esses argumentos serão números. Em seguida retorne o menor número 
entre todos os recebidos.
"""

def menor(*args):
    return min(args)

print(menor(960,203,50))

"""
4 - Crie uma função que calcule a formula de Bhaskara, encontrado o X. 
Os coeficientes a, b e c devem ser lidos por input.
"""

import math
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

x1 = (-b + math.sqrt(math.pow(b,2) - 4*a*c))/ (2*a)
x2 = (-b - math.sqrt(math.pow(b,2) - 4*a*c))/ (2*a)
print("A solução encontrada é ", x1, x2)

"""
5 - Crie uma função que receba uma string, e para cada letra minúscula a 
transforme em uma letra maiúscula e vice versa.
"""

def transformacao(texto):
    return texto.swapcase()

print(transformacao("olaMuNdo"))