# módulos são bibliotecas prontas para serem utilizadas

import datetime as data # módulo se chama datetime. usando álias com módulo(dando nome para módulo)
print(type(data))
data = data.datetime.now()
print(data)

import random
print(random.randrange(10,100)) #usando função que está dentro do módulo

from random import randrange #importando randrange diretamente do módulo
print(randrange(10,100))

from random import randrange as numero_aleatorio #importando randrange e atribuindo álias
print(numero_aleatorio(10,100))

from random import randrange,randint #importando mais de uma funções do módulo
print(randrange(10,100))