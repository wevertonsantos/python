# Perguntando para o usuário qual é o nome dele
name = input("What's your name? ") #input - recebendo o que foi passado e atribuindo a variável

# Mostrando hello para o usuário
print("hello, " + name) # concatenação de string
print("hello,", name)

# print(*objects, sep=' ', end='\n', file=None, flush=False)
# https://docs.python.org/3/library/functions.html#print
print("hello, ", end="") 
print(name)
print("hello,",name, sep="???")

print('hello, "friend"') #representação de aspas
print("hello, \"friend\"")

print(f"hello, {name}") # concatenação f-string