# 1 - Crie um programa que possui duas variáveis, uma recebe o ano 
# em que estamos e a outra o ano em que você nasceu. 
# Em seguida subtraia ambas para receber uma estimativa de quantos anos você tem. 
# Mostre esse valor na saída do programa.

ano_atual = 2025
data_nascimento = 2002
idade = ano_atual - data_nascimento
print("Estimativa de idade: {} anos".format(idade))

# 2 - Crie um programa que faz a média aritmética entre três números. 
# Estes números devem ser salvos em uma variável. 
# Mostre esse valor na saída do programa.

a = 5
b = 10
c = 7
media = (5 + 10 + 7) / 3
print("Média aritmética: %.1f" % (media))

# 3 - Crie um programa que calcule o IMC (índice de massa corporal).
# O IMC é dado pelo peso em KG divido pela altura em metros elevado ao quadrado. 
# Salvar esses valores em uma variável. Mostre esse valor na saída do programa.

peso = 75
altura = 1.80
imc = peso // altura ** 2
print("IMC: {}".format(imc))

# 4 (Desafio) - Você tem um determinado números de ovos de páscoa para dividir 
# entre um determinado número de pessoas (duas variáveis iniciais). 
# Determine quantos ovos ficarão por pessoa e quantos ovos sobrarão 
# pois não puderam ser divido igualmente. 
# Lembre que o número de ovos por pessoa é um número inteiro

ovos = 10
pessoas = 5
ovos_por_pessoa = ovos // pessoas
print("Ovos por pessoa: {}".format(ovos_por_pessoa))
ovos_restantes = ovos % pessoas
print("Ovo(s) que sobraram: {}".format(ovos_restantes))