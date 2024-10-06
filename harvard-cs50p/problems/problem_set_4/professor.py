#https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

#level = input("Level: ")
problems = []
while True:
    level = input("Level: ")
    if int(level) == 1 or int(level) == 2 or int(level) == 3:
        for i in range(10):
            x = random.randint(1,int(10))
            y = random.randint(1,int(10))
            problems.append([x,y])
        break

times = 1
score = 0
for problem in problems:
    x = problem[0]
    y = problem[1]
    result = x + y
    answer = int(input(f"{x} + {y} = "))
    while True:
        if answer != result:
            print("EEE")
            answer = input(f"{x} + {y} = ")
            times += 1
            if times == 3:
                print("EEE")
                print(f"{x} + {y} = {result}")
                answer = result
                times = 0
        else:
            score += 1
            break
    break
print(f"Score: {score}")