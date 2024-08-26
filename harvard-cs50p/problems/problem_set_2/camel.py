#https://cs50.harvard.edu/python/2022/psets/2/camel/

def main():
    name = input("camelCase: ")
    print(camel_case(name))

def camel_case(name):
    first_time = False
    words_capitalize = ""
    word_lower = ""
    snake_case = ""
    for n in name:
        if first_time == False:
            if name.islower():
                word_lower = name
            #Pegar a letra que está em maiúscula
            else: 
                word_capitalize = name[name.index(n):]
                word_lower = name[:name.index(n)]
                #Pegar da letra maiúscula até o restante da string
                if word_capitalize not in words_capitalize:
                    for word in word_capitalize:
                        #Se a próxima palavra for maiúscula, colocar um "_" antes dela 
                        if not word.isupper():
                            words_capitalize += word.lower()
                        else:
                            words_capitalize += f"_{word.lower()}"
                first_time = True
    if words_capitalize == "":
        snake_case = word_lower
        return snake_case
    else:
        snake_case = f"{word_lower}{words_capitalize}"
        return snake_case

main()