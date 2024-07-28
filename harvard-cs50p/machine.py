emoji = "?.?"
def main():
    global emoji #variável global acessível dentro da função para alterar o valor da variável
    say("Is anyone there?")
    emoji = "=)"
    say("Oh, hey!")

def say(phrase):
    print(f"{phrase} {emoji}")

main()