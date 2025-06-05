# 1 - Crie um programa que receba uma string por input e conte quantos caracteres ela têm, não leve em conta caracteres de espaço. Você não deve usar o len().

texto = input("Digite algum texto: ")
caracter = 0
for i in texto:
    if i != " ":
        caracter += 1
print("Esse texto tem exatamente %d caracter(es)" % caracter)

# 2 - Crie um programa que faça o calculo do fatorial de um número. O fatorial a ser calculado deve ser recebido por input.

fatorial = int(input("Digite o fatorial a ser calculado: "))
resultado = 1
for i in range(1,fatorial + 1):
    resultado *= i
print("O fatorial de %d é %d " % (fatorial, resultado))

# 3 - Crie um programa que leia um quantidade arbitraria de textos e concatene eles numa string única.
quantidade = int(input("Digite a quantidade de textos: "))
string = ''
for i in range(0,quantidade):
    string += input("Digite um texto: ")
print("Texto completo: %s" % string)

# 4 - Crie um programa que printe a tabuada da divisão de um número lido por input.
tabuada = int(input("Digite a tabuada de divisão desejada: "))
for x in range (1,11):
    print("%d / %d = %f " % (x, tabuada, x / tabuada))

# 5 - Crie um programa que percorra os números de 3 até 30 e diga se o número é primo ou não.
for numero in range(3,31):
  primo = True

  for num_teste in range(2, numero):
    if (numero % num_teste == 0):
      primo = False
      break
  
  if (primo):
    print("O número %d é primo" % (numero))
  else:
    print("O número %d não é primo " % (numero))