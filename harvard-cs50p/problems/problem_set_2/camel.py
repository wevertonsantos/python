#https://cs50.harvard.edu/python/2022/psets/2/camel/

def main():
    name = input("camelCase: ")
    print(camel_case(name))

def camel_case(name):
    ...

#main()

#Pegar a string da variável
name = "camelCase"
words_capitalize = ""
words_lower = ""
for n in name:
    #Pegar a letra que está em maiúscula
    if n.isupper():
        #Pegar da letra maiúscula até o restante da string
        if name[name.index(n):] not in words_capitalize:
            words_capitalize = name[name.index(n):]
            words_lower = name[:name.index(n)]
print(f"{words_lower}_{words_capitalize.lower()}")