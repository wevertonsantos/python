'''
Escreva num arquivo os números de 0 até 100. Uma linha para cada número.
'''

with open("0_ate_100.txt", "w") as arquivo:
    for i in range(0,100 + 1):
        if i != 100:
            arquivo.writelines(f"{str(i)}\n")
        else:
            arquivo.writelines(f"{str(i)}")