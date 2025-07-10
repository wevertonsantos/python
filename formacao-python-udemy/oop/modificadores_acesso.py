class Segredo:
    def __init__(self):
        self.__segredo = 'Senha' # propriedade privada

    def __printa_segredo(self): # função privada
        print(self.__segredo)

    def printa_segredo(self):
        self.__printa_segredo()


seg = Segredo()
print(seg.__segredo)