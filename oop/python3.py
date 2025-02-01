#utilizando python3 para criar classe

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(f"Meu nome é: {self.nome}, tenho {self.idade} anos e meu e-mail é: {self.email}")

cliente_1 = Cliente(nome = "Guilherme", email="email@gmail.com", idade = 20)

cliente_1.exibir()