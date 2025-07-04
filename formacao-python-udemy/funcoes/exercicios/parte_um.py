'''
1 - Crie uma função chamada “e_negativo” que receba um número, retorna um booleano “True” se o número for negativo, caso contrário retorna “False”.
'''

def e_negativo(num):
 if num < 0:
  return True
 else:
  return False
 
print(e_negativo(-1))
print(e_negativo(0))

# 2 - Crie um função que receba um array de números (int ou float) e retorne sua soma.

def soma(array):
    total = 0
    if type(array) == list:
        for num in array:
            total += num
    return total

array = [1,10,50,3]
print("Soma:",soma(array))

# 3 - Crie um função que receba uma string e que conte e retorne o número de vogais desta string.

def vogais(string):
    total = 0
    string = string.lower()
    vogais = ['a','e','i','o','u']
    for letra in string:
        if letra in vogais:
            total += 1
    return total

print("Quantidade de vogais na string:", vogais("ooolaa muundoo"))

# 4 - Crie um função que retorne o último caractere de um string recebida.

def caractere(string):
   return string[-1]

print('Último caractere da string recebida:',caractere("tudo bem?"))

# 5 - Crie um função que receba dois números e uma string dizendo se deve realizar a soma ou subtração do números.

def operacao(num1,num2,op):
    return num1 - num2 if op == '-' else num1 + num2
    
print('Operação:', operacao(10,5,'-'))