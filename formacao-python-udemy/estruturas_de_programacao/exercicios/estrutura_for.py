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

# 3 - Crie um programa que leia um quantidade arbitraria de textos e concatene eles numa string única.
quantidade = int(input("Digite a quantidade de textos: "))
string = ''
for i in range(0,quantidade):
    string += input("Digite um texto: ")
print("Texto completo: %s" % string)

# 4 - Crie um programa que printe a tabuada da divisão de um número lido por input.
tabuada = int(input("Digite qual tabuada gostaria de ver: "))
for x in range (1,tabuada + 1):
    for y in range(1,11):
        print("%d / %d = %d" % x,y,x/y)

# 5 - Crie um programa que percorra os números de 3 até 30 e diga se o número é primo ou não.
for i in range(3, 31):
    print(i)
    if i % 2 != 0:
        print(i)