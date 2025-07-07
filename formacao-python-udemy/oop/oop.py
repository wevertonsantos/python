class Teste: # criando classe(objeto) bem simples
    pass

minha_classe = Teste() # instância do objeto
print(type(minha_classe))

class NossaClasse: # criando classe
    def __init__(self): # criando construtor
        print("Eu existo")

var = NossaClasse()