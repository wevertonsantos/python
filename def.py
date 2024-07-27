def main(): # função main
    name = input("What's your name? ")
    hello(name)

def hello(name="world"): #função com argumento padrão
    print(f"Hello, {name}")

main() #chamando a função para executar a pilha de código