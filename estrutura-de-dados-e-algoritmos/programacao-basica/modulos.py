'''
biblioteca math
'''
import math

#raiz quadrada
print(math.sqrt(9))
#seno
print(math.sin(45))
#cosseno
print(math.cos(45))
#logaritmos
print(math.log(1000,10))
print(math.log(32,2))
print(math.log(1000))
#pi
print(math.pi)

'''
biblioteca datetime
'''
import datetime

#recursos existente na biblioteca
print(dir(datetime))
#data de hoje
print(datetime.date.today())
#data e hora
print(datetime.datetime.now())

data = datetime.date(2026, 2,1)
print(data)
#dia
print(data.day)
#mes
print(data.month)
#ano
print(data.year)

horario = datetime.datetime(2026,2,1,18,43,0)
print(horario)

#hora
print(horario.hour)
#minuto
print(horario.minute)
#segundos
print(horario.second)

'''
biblioteca random
'''

import random

#números de 0 a 1
print(random.random())
#números random de uma faixa que você queira
print(random.randint(1,10))
#números random com faixa e com step
print(random.randrange(0,10,2))
#sortear elemento dentro de uma lista
x = ['K','d',13,'34-j','x']
print(random.choice(x))

'''
biblioteca time
'''

import time as tm

#tempo atual em segundos
print(tm.time())
#ver quanto tempo código leva para executar
antes = tm.time()
lista = []
for i in range(0,100000):
    lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f"Tempo: {intervalo} segundos")

print('Finalizando...')
#parar o programa por tempo
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')

'''
biblioteca própria
'''

import exercicios.parte6 as parte6

print(parte6.mensagem("Mensagem"))
print(parte6.mensagem_float(2.5))