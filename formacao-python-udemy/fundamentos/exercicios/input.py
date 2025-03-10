'''
1 - Crie um programa que leia por input
dois números e realize a divisão entre ambos.
Formate o print para mostrar o cálculo completo.
'''

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
print("Cálculo da divisão: %.2f" % (x/y))

'''
2 - Crie um programa que mostre o dia, mês, ano,
hora, minuto e segundos inseridos pelo usuário.
Formate o valor.
'''

dia = input("Escreva o dia: ")
mes = input("Escreva o mês: ")
ano = input("Escreva o ano: ")
hora = input("Escreva a hora: ")
minuto = input("Escreva a minuto: ")
segundos = input("Escreva os segundos: ")
print("%s/%s/%s %s:%s:%s" % (dia,mes,ano,hora,minuto,segundos))