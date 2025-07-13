numero = 10
del numero # deletando variável da memória
# print(numero) irá dar erro

class Teste:
    def __init__(self):
        self.lista = [1,2,3]
    def __del__(self): # evento especificando quando a classe for deletada
        print("Fui deletado")

variavel = Teste()
del variavel # deletando instância do objeto