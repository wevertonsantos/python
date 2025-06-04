# 1 - Crie um programa que receba uma string por input e conte quantos caracteres ela têm, não leve em conta caracteres de espaço. Você não deve usar o len().

texto = input("Digite algum texto: ")
caracter = 0
for i in texto:
    if i != " ":
        caracter += 1
print("Esse texto tem exatamente %d caracter(es)" % caracter)