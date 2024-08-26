#https://cs50.harvard.edu/python/2022/psets/2/camel/

def main():
    name = input("camelCase: ")
    print(camel_case(name))

def camel_case(name):
    ...

#main()

#Pegar a string da variável
name = "camelCaseAeseCase"
words_capitalize = ""
word_lower = ""
snake_case = ""
for n in name:
    #Pegar a letra que está em maiúscula
    if n.isupper():
        word_capitalize = name[name.index(n):]
        #Pegar da letra maiúscula até o restante da string
        if word_capitalize not in words_capitalize:
            for word in word_capitalize:
                #Se a próxima palavra for maiúscula, colocar um "_" antes dela 
                words_capitalize += word
                # A cada palavra com a primeira letra maiúscula, colocar "_"

print(snake_case)