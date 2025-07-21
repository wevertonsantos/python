# fazendo join

texto1 = "olá"
print("#".join(texto1)) # a cada letra do texto1 irá colocar #

lista = ['a','b','c','d']
letras = ' '.join(lista) # a cada letra da lista irá ter espaço
print(letras)

letras = '-'.join([str(i) for i in range(10)])
print(letras)