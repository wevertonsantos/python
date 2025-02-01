from categoria import Categoria
from transacao import Transacao

lista_categorias = []
lista_transacoes = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)
    lista_categorias.append(nova_categoria)

def cadastrar_transacao():
    nova_transacao = Transacao()

def saldo_total():
    ...