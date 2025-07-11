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