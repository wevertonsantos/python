class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def print_nome(self):
        print(f"Meu nome é: {self.nome}")

pessoa1 = Pessoa("Rodrigo","34")
pessoa1.print_nome() # chamando função da instância do objeto