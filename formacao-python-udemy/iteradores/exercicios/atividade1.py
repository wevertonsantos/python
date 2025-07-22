# 1 - Crie uma função iterável “meses” que retorne meses. 
# Use um laço for para mostrar os valores.

def meses():
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto','setembro','outubro','novembro','dezembro']
    for i in meses:
        yield i

for mes in meses():
  print(mes)