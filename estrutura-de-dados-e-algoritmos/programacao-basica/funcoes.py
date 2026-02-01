#funcões sem parâmetro e sem retorno
def mensagem():
    print('Texto da função')

mensagem()

#função com passagem de parâmetro
def mensagem(texto):
    print(texto)

mensagem('Texto 1')

def soma(a,b):
    print(a + b)

soma(2,2)

#função com passagem de parâmetros e retorno

def soma(a,b):
    return a + b

print(soma(2,2))

r = soma(3,2)
print(r)