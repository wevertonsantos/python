# 1 - Crie uma função iterável “meses” que retorne meses. 
# Use um laço for para mostrar os valores.

def meses():
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto','setembro','outubro','novembro','dezembro']
    for i in meses:
        yield i

for mes in meses():
  print(mes)

# 2 - Cria uma função iterável que receba uma lista de números e que retorne 
# a cada iteração um item dessa lista multiplicado por dois.

def duplicado(lista):
  for i in lista:
    yield i*2

lista = [1,2,3,4,5]

for i in duplicado(lista):
  print(i)