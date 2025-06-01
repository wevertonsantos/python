# 1 - Crie um única string que contêm seu nome e sobrenome, em seguida use o slicing para separar o nome em uma variável e o seu sobrenome em outra. Printe esses valores.

nome_completo = "Weverton Santos"
nome = nome_completo[:8]
sobrenome = nome_completo[9:]
print(nome,sobrenome)

# 2 - Leia uma string através do input e retire o ultimo caractere.

string = input("Digite alguma coisa: ")
print(string[:-1])
