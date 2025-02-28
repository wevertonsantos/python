# 1 - Crie um programa que possui uma variável do “tipo string” 
# contendo um número que indique quanto você tem no banco. 
# Em seguida desconte mil deste valor e mostre na saída do programa.

saldo = "2000"
saldo_descontado = float(saldo) - 1000
print("Total restado:",saldo_descontado)

# 2 - Crie um programa que indique se seu saldo bancário esta zerado (valor lógico). 
# Declare uma variável para guardar seu saldo bancário.

saldo = 2000
print("Saldo bancário zerado?", not bool(saldo))

# 3 - Crie um programa que contenha sua altura, mas deve somente mostrar 
# a parte inteira de sua altura na saída do programa, 
# pois queremos uma estimativa.

altura = 1.80
print("Parte inteira da altura:",int(altura))