#https://cs50.harvard.edu/python/2022/psets/4/game/
import random

level = input("Level: ")
guess = None
while True:
    if level.isnumeric():
        random_number = random.randint(1,int(level))
        if guess == None:
            guess = input("Guess: ")
        else:
            if guess.isnumeric():
                guess = int(guess)
                if guess < random_number:
                    print("Too small!")
                elif guess > random_number:
                    print("Too large!")
                else:
                    print("Just right!")
                break
            else:
                guess = input("Guess: ")
    else:
        level = input("Level: ")