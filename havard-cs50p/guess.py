def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    number = 10
    if guess == number:
        print("Win")
    else:
        print("Try again")

main()