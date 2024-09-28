#https://cs50.harvard.edu/python/2022/psets/4/game/
import random

level = input("Level: ")
guess = input("Guess: ")
while True:
    try:
        level = int(level)
        guess = int(guess)
        random_number = random.randint(1,level)
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Just right!")
        break
    except ValueError:
        level = input("Level: ")