# módulos são bibliotecas prontas para serem utilizadas

import datetime as data # módulo se chama datetime. usando álias com módulo(dando nome para módulo)
print(type(data))
data = data.datetime.now()
print(data)

import random
print(random.randrange(10,100)) #usando função que está dentro do módulo

from random import randrange #importando randrange diretamente do módulo
print(randrange(10,100))