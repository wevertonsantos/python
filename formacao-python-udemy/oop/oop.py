class Teste: # criando classe(objeto) bem simples
    pass

minha_classe = Teste() # instância do objeto
print(type(minha_classe))

class NossaClasse: # criando classe
    def __init__(self): # criando construtor
        print("Eu existo")

var = NossaClasse()

class Pessoa:
    especie = "Homo Sapiens" # atributo estático
    num_pessoas = 0 # outro atributo estático
    def __init__(self,nome,idade): # atribuindo parâmetros
        self.nome = nome # self é o próprio objeto que recebe nome
        self.idade = idade
        print("Pessoa com nome %s e idade %d criada" % (nome,idade))
        Pessoa.num_pessoas += 1 # a cada instância atribuí 1

pessoa1 = Pessoa('Rodrigo',25) # chamando instância do objeto
print(Pessoa.num_pessoas)
pessoa2 = Pessoa('Lucas',21)


# acessando propriedades
print(pessoa1.nome)
print(pessoa2.idade)

# alterando propriedades
pessoa1.nome = "Marcelo"
print(pessoa1.nome)