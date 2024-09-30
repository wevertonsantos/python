#https://cs50.harvard.edu/python/2022/psets/4/game/
import random

level = input("Level: ")
guess = None
while True:
    if level.isnumeric():
        random_number = random.randint(1,int(level))
        if guess == None:
            guess = input("Guess: ")
        if guess.isnumeric():
            while True:
                if int(guess) < random_number:
                    print("Too small!")
                    guess = input("Guess: ")
                elif int(guess) > random_number:
                    print("Too large!")
                    guess = input("Guess: ")
                else:    
                    print("Just right!")
                    break
            break
        else:
            guess = input("Guess: ")
    else:
        level = input("Level: ")