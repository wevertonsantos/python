#https://docs.python.org/3/library/stdtypes.html#string-methods

#Pergunta pelo nome do usuário
#name = input("What's your name? ")
name = "Wev"
name = name.strip() #Remove o espaço em branco da string (esquerda e da direita) e incluí na variável
print(f"hello, {name}")

#Coloca a primeira letra em maiúsculo na string
name = name.capitalize()
print(f"hello, {name}")

#Coloca cada palavra com a primeira letra em maiúsculo
name = name.title()
print(f"hello, {name}")

#Juntando funções
name = name.strip().title()
print(f"hello, {name}")

#Outra forma de utilizar
name = input("What's your name? ").strip().title()
primeiro, utltimo = name.split(" ")
print(f"hello, {primeiro}")