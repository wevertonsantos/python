class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def print_nome(self):
        print(f"Meu nome é: {self.nome}")