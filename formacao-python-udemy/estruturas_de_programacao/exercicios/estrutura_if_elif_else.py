# 1 - Crie um programa que receba o seu saldo bancário e o quanto você deve. 
# Em seguida o programa deve dizer se você tem saldo positivo ou negativo.

saldo_bancario = int(input("Digite o seu saldo: "))
quanto_devo = int(input("Digite o quanto você deve: "))
if saldo_bancario > quanto_devo:
    print("Saldo positivo")
else:
    print("Saldo negativo")

# 2 - Crie um programa que possui uma variável que guarde seu CPF e que guarde 
# uma senha de sua escolha. Em seguida receba por input uma senha do usuário. 
# Caso a senha recebida seja a correta mostre o CPF, 
# caso não diga que a senha esta incorreta.

cpf = "555.444.555-55"
senha = "232323"
senha_recebida = input("Digite uma senha: ")

if senha == senha_recebida:
    print(cpf)
else:
    print("Senha está incorreta")

# 3 - Crie um programa que fale sobre sua idade. As regras são as seguintes
# você deve receber por input sua idade, se você tiver ate três anos 
# printe que é um bebe, ate 13 anos uma criança, ate 18 anos adolescente, 
# até 65 adulto. Em nenhum deste casos é um idoso

idade = int(input("Digite sua idade: "))
if idade <= 3:
    print("Você é um bebê")
elif idade <= 13:
    print("Você é uma criança")
elif idade <= 18:
    print("Você é um adolescente")
elif idade <= 65:
    print("Você é um adulto")
else:
    print("Você é um idoso")

# 4 - Crie um programa que receba dois números, e também receba do usuário 
# a operação que deve ser feita, as possibilidades são soma(+), subtração (-), 
# divisão(/) e multiplicação(*). 
# Realize a operação escolhida sobre os dois números.

numero1 = int(input("Digite primeiro número: "))
numero2 = int(input("Digite segundo número: "))
operacao = input("Digite a operação para realizar: ")

if operacao == "+":
    print("A soma de %d + %d, é: %d" % (numero1,numero2,numero1 + numero2))
elif operacao == "-":
   print("A soma de %d - %d, é: %d" % (numero1,numero2,numero1 - numero2))
elif operacao == "/":
    print("A soma de %d / %d, é: %d" % (numero1,numero2,numero1 / numero2))
elif operacao == "*":
    print("A soma de %d * %d, é: %d" % (numero1,numero2,numero1 * numero2))
else:
    print("Operação inválida")