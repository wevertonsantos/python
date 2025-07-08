class Tipo1:
    def __init__(self, outra_classe):
        self.outra = outra_classe # propriedade que é outra classe

class Tipo2:
    numero = 10

classe2 = Tipo2()
classe1 = Tipo1(classe2) # passando a instância da classe como parâmetro.
print(classe1.outra.numero) # printando propriedade número atráves da classe

class Exemplo:
    def __init__(self):
        pass

lista = []
ex1 = Exemplo
ex2 = Exemplo
lista.append(ex1) # atribuindo uma instância da classe dentro da lista
lista.append(ex2)
print(lista)