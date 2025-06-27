'''
6 - Crie um função que receba uma lista de elementos e um valor qualquer. Em 
seguida retorne um booleano dizendo se o valor foi encontrado ou não na lista.
'''

def encontrando(array,valor):
    return True if valor in array else False
    
print(encontrando([10,20,3,4,5,6],2))

'''
7 - Crie um função que receba uma lista de elementos e um valor qualquer. Em 
seguida retorne um booleano dizendo se o valor foi encontrado ou não e também 
a posição onde foi encontrado.
'''

def encontrando(array,valor):
    if valor in array:
        return True, array.index(valor)
    else: 
        return False
    
print(encontrando([10,20,3,4,5,6],2))

'''
8 - Crie uma função que recebe um número arbitrário de parâmetros. Em seguida diga qual o tipo de cada parâmetro
'''

def typing(*args):
    for arg in args:
        print((type(arg)))

typing(1,'for',True)

'''
9 - Crie uma função que receba um string, mas que possua um decorator para 
transforma-la em uma citação, ou seja você deve retornas strings entre aspas 
duplas, além disso transforme todos os caracteres para minúscula usando a 
função lower()
'''

def citacao(func):
    def inner_func(texto):
        return '"' + func(texto).lower() + '"'
    return inner_func

@citacao
def transforma(texto):
    return texto

print(transforma("OLÁ, ISTO É UMA CITAÇÃO"))

'''
10 - Cria uma função recursiva que intere os números de 0 até 10 e printe o 
resultado de sua divisão inteira com o número três
'''

def divisao(num):
    print(num // 3)
    if num >= 10:
        return
    divisao(num + 1)

divisao(0)