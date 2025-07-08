class FormaGeometrica:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

class Quadrado(FormaGeometrica): # herdando outra classe
    lado = 10 # criando propriedade

class Triangulo(FormaGeometrica):
    angulo = 30

quadrado = Quadrado(100,50) # instânciando com as propriedades da classe pai
triangulo = Triangulo(100,50)

print(quadrado.altura)
print(quadrado.largura)
print(quadrado.lado)