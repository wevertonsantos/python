'''
Leia o seguinte arquivo (“exercicio1.txt”) e transforme em uma lista.
'''

with open("exercicio1.txt","r") as arquivo:
    lista = []
    arquivo_lido = arquivo.read()
    for linha in arquivo_lido:
        if linha != "\n":
            lista.append(int(linha))
    print(lista)