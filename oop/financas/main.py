from categoria import Categoria
from transacao import Transacao

c = Categoria(nome="Receitas")

t1 = Transacao(
    descricao="Salário Jan/2025",
    valor=1000,
    categoria=c
)

t1.exibir()