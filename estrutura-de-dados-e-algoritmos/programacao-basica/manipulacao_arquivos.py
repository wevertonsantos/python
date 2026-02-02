#dando nome ao arquivo que está sendo aberto com with
with open('./frase1.txt') as file:
    for linha in file:
        print(linha)

with open('./frase1.txt') as file:
    r = file.readlines()
    print(r)

#criando arquivo com modo write
with open('./texto2.txt','w') as file:
    file.write("Olá a todos")