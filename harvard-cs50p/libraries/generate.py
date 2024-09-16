#https://docs.python.org/3/library/random.html
import random #importando módulo

coin = random.choice(["heads","tails"]) #choices
print(coin)

number = random.randint(1,10) #random number between 1 and 10
print(number)

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)