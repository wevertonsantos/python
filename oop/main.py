class Cliente:
    def __init__(self,nome,email): #construtor
        self.nome = nome
        self.email = email

    def exibir(self):
        print(self.email, self.idade)

cliente_1 = Cliente("Guilherme","email@email.com") #objeto

print(cliente_1)