class FormaGeometrica:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    def calcula_area(self):
        pass

class Quadrado(FormaGeometrica):
    def calcula_area(self): # fazendo override da classe pai
        return self.altura * self.largura
    
quadrado = Quadrado(200,200)
print(quadrado.calcula_area())