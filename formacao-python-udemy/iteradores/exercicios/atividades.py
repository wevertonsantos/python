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

# 3 - Crie uma classe iterável chamada “Tabuada” que calcule a tabuada da 
# multiplicação do número recebido no construtor. 
# A cada iteração ela deve retornar um resultado da tabuada. 
# Para testar use um laço for.

class Tabuada:
  def __init__(self, num):
    self.num = num
  def __iter__(self):
    self.atual = 0
    return self
  def __next__(self):
    self.atual += 1
    if(self.atual ==11):
      raise StopIteration
    return self.atual * self.num

tabuada_cal = Tabuada(2)

for i in tabuada_cal:
  print(i)

# 4 (Desafio) - Crie uma classe que retorne os fatoriais de um número no 
#  intervalo de X a Y, recebidos por parâmetro no construtor da classe.

class Fatorial:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def __iter__(self):
    self.atual = self.x
    return self
  
  @staticmethod
  def calcula_fatorial(num):
    result = 1
    for i in range(1, num+1):
      result *= i
    return result
  
  def __next__(self):
    if (self.atual == self.y + 1):
      raise StopIteration
    result = Fatorial.calcula_fatorial(self.atual)
    self.atual += 1
    return result

for i in Fatorial(1,10):
  print(i)

# 5 - Utilizando como base o exercício 1, retorne o número que representa o mês 
# e o próprio mês. Faça isso de duas maneiras diferentes 
# (usando enumeradores e a outra usando join).

def meses_enum():
  meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto','setembro','outubro','novembro','dezembro']
  for i in enumerate(meses):
    yield i

for indice, mes in meses_enum():
  print(indice+1, mes)