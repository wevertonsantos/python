class Natural:
    def __init__(self,numero):
        self.__numero = numero # propriedade privada

    @property #decorator utilizado para ler o valor da variável privada número
    def numero(self):
        print("Pegando número")
        return self.__numero
    
    @numero.setter
    def numero(self,value):
        if value >= 0:
            self.__numero = value
            print('Setando número para',value)

numero = Natural(10)
numero.numero = 20 # invocando método set
print(numero.numero) # invocando método get

class Pessoa:
    def __init__(self,nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome.capitalize()
    
    @nome.setter
    def nome(self,value):
        if len(value) != 0:
            self.__nome = value

pessoa = Pessoa("rodrigo")
print(pessoa.nome)
pessoa.nome = 'fernando'
print(pessoa.nome) 