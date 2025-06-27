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