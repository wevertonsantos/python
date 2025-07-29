from os import path
arquivo_existe = path.exists("exemplo.txt") # verificando se arquivo existe

if arquivo_existe:
    print("O arquivo existe")
else:
    print("O arquivo não existe")

file = open("teste.txt",'wt')
try:
    file.write('hello, world')
finally:
    file.close() # fechando mesmo se houver erro