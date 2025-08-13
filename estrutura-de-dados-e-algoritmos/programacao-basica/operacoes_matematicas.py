a = 5
b = 3
print(a,b)
print(a+b)
print('A soma é', a + b)
print('A subtração é', a - b)
print('A divisão é', a / b)
print('A multiplicação é',a * b)
print('O resto da divisão é',10 % 2)
print('5 elevado a 3 é', 5**3)

import math # importar funções matemáticas
print(math.sqrt(81)) #raiz quadrada

# arredondamento
casos_doenca = 134
numero_habitantes = 34432
casos_por_habitantes = casos_doenca / numero_habitantes
print(casos_por_habitantes)
print(round(casos_por_habitantes,6)) # arredondamento para 6 casas
print('O número de casos por habitante é de', round(casos_por_habitantes,4))