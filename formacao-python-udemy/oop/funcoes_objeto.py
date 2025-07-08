class Pessoa:
    def __init__(self,nome):
        self.nome = nome
    def print_string(self,nome):
        print(f"Meu nome é: {nome}")
    def print_nome(self):
        self.print_string(self.nome) # chamando função do próprio objeto
    def insere_idade(self,idade):
        self.idade = idade # criando propriedade dentro da classe

pessoa1 = Pessoa("Rodrigo")
pessoa1.print_nome() # chamando função da instância do objeto