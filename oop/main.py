class Cliente:
    def __init__(self,nome,email): #construtor
        self.nome = nome
        self.email = email

    def exibir(self): #método
        print(self.nome, self.email)

cliente_1 = Cliente("Guilherme","email@email.com") #objeto