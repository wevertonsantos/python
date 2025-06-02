if (True):
    print("Este código vai ser executado")

if (False):
    print("Este código não vai ser executado")

if (True):
    pass #estrutura quando não executa nada

#avaliação lógica com if (executa quando é verdadeiro)
valor1 = 10
valor2 = 10
sao_iguais = (valor1 == valor2)
if sao_iguais:
    print("São iguais")

if (valor1 == valor2):
    print("São iguais")

if (10 != 20):
    print("São diferentes")

if (10 != 10):
    print("Não irá executar porque é falso")

numero = 11
if (numero > 10):
    print("Número é maior que 10")

nome = input("Digite seu nome: ")
if "a" in nome:
    print("Tem a letra 'a'")