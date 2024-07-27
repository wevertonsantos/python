def main(): # função main
    name = input("What's your name? ")
    hello(name)
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    caculator(x,y)

def hello(name="world"): #função com argumento padrão
    print(f"Hello, {name}")

def caculator(x,y): # função com retorno
    return print(x + y)

main() #chamando a função para executar a pilha de códigos 