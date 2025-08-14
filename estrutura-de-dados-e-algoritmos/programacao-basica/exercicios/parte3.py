'''
Ler 5 notas e informar a média
'''

soma = 0
for i in range(1,6):
    nota = float(input("Digite a nota: "))
    soma += nota
media = soma / 5
print('A média é:', media)

soma = 0
i = 1
while i < 6:
    nota = float(input("Digite a nota: "))
    soma += nota
    i += 1
media = soma / 5
print('A média é:', media)

'''
Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
'''

for i in range(1,10 + 1):
    print(f"3 x {i} = {3*i}")

i = 1
while i < 11:
    print(f"3 x {i} = {3*i}")
    i += 1  