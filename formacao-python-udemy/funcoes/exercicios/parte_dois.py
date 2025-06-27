'''
6 - Crie um função que receba uma lista de elementos e um valor qualquer. Em 
seguida retorne um booleano dizendo se o valor foi encontrado ou não na lista.
'''

def encontrando_valor(array,valor):
    return True if valor in array else False
    
print(encontrando_valor([10,20,3,4,5,6],2))