class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def print_string(self,nome):
        print(f"Meu nome é: {nome}")
    def print_nome(self):
        self.print_string(self.nome) # chamando função do próprio objeto

pessoa1 = Pessoa("Rodrigo","34")
pessoa1.print_nome() # chamando função da instância do objeto