'''
Leia o seguinte arquivo (“exercicio2.txt”), onde cada linha tem um produto e seu
valor. Crie uma classe chamada Produto, para representar cada item do arquivo, com
nome e valor. Salve todos produtos em uma lista, ao final imprima a lista item por item,
mostrando nome e valor.
'''

class Produto:
  def __init__(self, nome, valor):
    self.nome = nome
    self.valor = valor

produtos = []

with open('exercicio2.txt','rt') as arquivo:
  for linha in arquivo:
    indice_separa = linha.index("R$")

    nome = linha[:indice_separa-1]
    valor = linha[indice_separa:len(linha)-1]
    produto = Produto(nome, valor)
    produtos.append(produto)

for produto in produtos:
  print(produto.nome, produto.valor)