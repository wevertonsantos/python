class Tipo1:
    def __init__(self, outra_classe):
        self.outra = outra_classe # propriedade que é outra classe

class Tipo2:
    numero = 10

classe2 = Tipo2()
classe1 = Tipo1(classe2) # passando a instância