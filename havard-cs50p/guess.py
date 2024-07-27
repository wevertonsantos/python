def get_guess():
    guess = int(input("Enter a guess: "))
    number = 10
    if guess == number:
        return "Win"
    else:
        return "Try again"

print(get_guess())