'''
1 - Crie uma função que receba duas strings que serão convertidas para
números para serem somadas, se ao realizar o casting ocorrer um erro, gere
uma exceção informando o motivo.
'''

def soma(s1,s2):
    try:
        return int(s1) + int(s2)
    except:
        print("Valores que você digitou não é válido")

print(soma('10','s'))

'''
2 - Crie uma função que receba uma lista e um número e retorne o elemento
da lista na posição deste número. Faça um tratamento para que caso haja um
acesso fora do índice a função retorne o valor None.
'''

def acesso_seguro(lista,indice):
    try:
        return lista[indice]
    except:
        return None

print(acesso_seguro([1,2,3,4,5,6],10))

'''
3 - Crie uma função que leia o input do usuário e retorne o que foi digitado, mas caso o input seja interrompido trate a exceção e retorne o valor None.
'''

def retornando_input():
    try:
        return input("Digite algo: ")
    except:
        return None
    
print(retornando_input())

'''
4 - Crie uma classe que represente um caractere (string de tamanho 1), use
propriedades ou crie uma função para isso (mas deixe valor privado) e caso
o usuário tente inserir um texto gere uma exceção dizendo o motivo.
'''

class Caracter:
  def __init__(self,caracter):
    self.__caracter = ''
    self.caracter = caracter
  
  @property
  def caracter(self):
    return self.__caracter

  @caracter.setter
  def caracter(self, value):
    if len(value)> 1:
      raise Exception("Caracter deve ter no máximo tamanho 1")
    self.__caracter = value

letra = Caracter("a")
print(letra.caracter)

try:
  letra.caracter = 'b'
except Exception as ex:
  print(str(ex))

print(letra.caracter)  