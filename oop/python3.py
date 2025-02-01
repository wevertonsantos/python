#utilizando python3 para criar classe

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

cliente_1 = Cliente(nome = "Guilherme", email="email@gmail.com", idade = 20)

print(cliente_1.nome,cliente_1.email,cliente_1.idade)