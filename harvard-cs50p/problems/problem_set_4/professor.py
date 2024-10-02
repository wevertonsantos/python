#https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

#level = input("Level: ")
problems = []
while True:
    level = input("Level: ")
    if int(level) == 1 or int(level) == 2 or int(level) == 3:
        while 0 < 9:
            x = random.randint(1,int(10))
            y = random.randint(1,int(10))
            problems.append([x,y])
            print(problems)
            break