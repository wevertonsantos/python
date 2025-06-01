# 1 - Crie um única string que contêm seu nome e sobrenome, em seguida use o slicing para separar o nome em uma variável e o seu sobrenome em outra. Printe esses valores.

nome_completo = "Weverton Santos"
nome = nome_completo[:8]
sobrenome = nome_completo[9:]
print(nome,sobrenome)

# 2 - Leia uma string através do input e retire o ultimo caractere.

string = input("Digite alguma coisa: ")
print(string[:-1])

# 3 - Faça um programa que leia uma string através do input e diga se ela possui uma vogal.

string = input("Digite alguma coisa: ")
print("String tem vogal?","A" in string or "E" in string or "I" in string or "O" in string or "U" in string or "a" in string or "e" in string or "i" in string or "o" in string or "u" in string)
