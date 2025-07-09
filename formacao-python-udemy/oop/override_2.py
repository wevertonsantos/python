class FormaGeometrica:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    def calcula_area(self):
        pass

class Quadrao(FormaGeometrica):
    def calcula_area(self): # fazendo override da classe pai
        return self.altura * self.largura