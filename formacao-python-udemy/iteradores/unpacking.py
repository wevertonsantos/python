produtos = [
    ['carro','200.000']
]

for produto,valor in produtos: # atribuindo produto e valor em duas variáveis
    print(produto,valor)

def gen1():
    yield [1,2]
    yield [3,4]
    yield [5,6]

for x,y in gen1(): #unpacking com yield
    print(x,y)