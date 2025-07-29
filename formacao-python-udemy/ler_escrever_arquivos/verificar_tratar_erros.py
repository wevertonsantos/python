from os import path
arquivo_existe = path.exists("exemplo.txt") # verificando se arquivo existe

if arquivo_existe:
    print("O arquivo existe")
else:
    print("O arquivo não existe")