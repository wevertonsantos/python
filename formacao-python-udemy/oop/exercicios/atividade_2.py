'''
2 - Cria uma classe que represente uma pessoa. Ela deve possuir um nome, 
CPF e um dependente, onde o dependente é outra pessoa. 
Dependente não é obrigatório. Crie duas instâncias: pai e filho, 
e imprima as saídas.
'''
class Pessoa:
    def __init__(self,nome,cpf,depedente=None):
        self.nome = nome
        self.cpf = cpf
        self.depedente = depedente

pai = Pessoa("Rodrigo","200320032")
filho = Pessoa("Rodrigo Junior","200320233",pai.nome)
print(f"Nome: {pai.nome} CPF: {pai.nome} Dependente: {pai.depedente}")
print(f"Nome: {filho.nome} CPF: {filho.cpf} Dependente: {filho.depedente}")