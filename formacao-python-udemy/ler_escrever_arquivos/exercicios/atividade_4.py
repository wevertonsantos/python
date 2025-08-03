'''
Escreva num arquivo todos números positivos e menores que 100 que são divisíveis por 3.
'''

with open('exercicio4.txt','wt') as arquivo:
  for i in range(0,101):
    if i % 3 == 0:
      arquivo.write(str(i) + '\n')