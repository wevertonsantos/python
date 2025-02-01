from funcionalidades import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total
)

#Cadastrando categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_viagens = cadastrar_categoria("Viagens")

#Cadastrando transações
cadastrar_transacao(
    descricao="Salário Jan/2025",
    valor=1000.0,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Conta de luz",
    valor=-150.0,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Recife/2025",
    valor=-1200.0,
    categoria=categoria_viagens
)

total = saldo_total()

print(f"Saldo total: {total}")