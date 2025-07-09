class ClassePai:
    def __init__(self):
        print("Sou a classe pai")

class ClasseFilha1(ClassePai):
    def __init__(self):
        print("Sou a classe filha 1") # sobrescrevendo método init

class ClasseFilha2(ClassePai):
    def __init__(self):
        print("Sou a classe filha 2")

pai = ClassePai()
filha1 = ClasseFilha1() # sobrescrevendo método init
filha2 = ClasseFilha2()

class FormaGeometrica():
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

class Quadrado(FormaGeometrica):
    def __init__(self,altura,largura,atributo_quadrado):
        FormaGeometrica.__init__(self, altura, largura) # instânciando o init da classe pai e as propriedades vão estar disponível
        self.atributo_quadrado = atributo_quadrado

quadrado = Quadrado(100,200,'quadrado') # instanciando e passando propriedades

print(quadrado.altura)
print(quadrado.atributo_quadrado)