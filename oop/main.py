class Cliente:
    def __init__(self,nome,email,idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def exibir(self):
        print(self.email, self.idade)