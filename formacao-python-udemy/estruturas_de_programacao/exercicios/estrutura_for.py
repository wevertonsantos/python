# 1 - Crie um programa que receba uma string por input e conte quantos caracteres ela têm, não leve em conta caracteres de espaço. Você não deve usar o len().

texto = input("Digite algum texto: ")
caracter = 0
for i in texto:
    if i != " ":
        caracter += 1
print("Esse texto tem exatamente %d caracter(es)" % caracter)

# 2 - Crie um programa que faça o calculo do fatorial de um número. O fatorial a ser calculado deve ser recebido por input.

fatorial = int(input("Digite o fatorial a ser calculado: "))
for i in range(1,fatorial):
    print(fatorial)
#    5 * 4 * 3 * 2 * 1