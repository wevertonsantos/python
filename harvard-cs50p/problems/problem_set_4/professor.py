#https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

#level = input("Level: ")
problems = []
while True:
    level = input("Level: ")
    if level.isnumeric():
        if int(level) == 1 or int(level) == 2 or int(level) == 3:
            for i in range(10):
                x = random.randint(1,int(10))
                y = random.randint(1,int(10))
                problems.append([x,y])
            break

times = 0
score = 0
error = False
for problem in problems:
    x = problem[0]
    y = problem[1]
    result = x + y
    while True:
        answer = input(f"{x} + {y} = ")
        if answer.isnumeric():
            if int(answer) != result:
                print("EEE")
                times += 1
                if times == 1:
                    answer = input(f"{x} + {y} = ")
                    if answer.isnumeric():
                        if answer == result:
                            score += 1
                            times = 0
                            break 
                    else:
                        times += 1
                        print("EEE")
                else:
                    print(f"{x} + {y} = {result}")
                    times = 0
                    break
            else:
                score += 1
                times = 0
                break
        else:
            print("EEE")
            times += 1
            if times == 3:
                print(f"{x} + {y} = {result}")
                times = 0
                break
            else:
                continue
            #se a resposta não é numérica,

            '''
            except ValueError:
            print("EEE")
            answer = input(f"{x} + {y} = ")
            times += 1
            if times > 0:
                if times == 1:
                    print("EEE")
                    answer = input(f"{x} + {y} = ")
                    times += 1
                else:
                    print("EEE")
                    answer = input(f"{x} + {y} = ")
            if answer != result:
                print("EEE")
                print(f"{x} + {y} = {result}")
                times = 0
            error = True
            break
            '''
        
print(f"Score: {score}")