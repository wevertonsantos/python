#https://cs50.harvard.edu/python/2022/psets/4/professor/
import random

def main():
   level = get_level()
   generate_integer(level)

def get_level():
    while True:
        level = input("Level: ")
        if level.isnumeric():
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                return level

def generate_integer(level):
    random_number = int(random.random())
    integer = random.randint(random_number,level)
    return integer

#for level in range(10):
        #x = random.randint(1,int(10))
        #y = random.randint(1,int(10))
        #problems.append([x,y])

main()

times = 0
score = 0
error = False
problems = []
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
                        if int(answer) == result:
                            score += 1
                            times = 0
                            break 
                        else:
                            times += 1
                            print("EEE")
                    else:
                        times += 1
                        print("EEE")
                elif times == 2:
                    times += 1
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
            if times >= 3:
                print(f"{x} + {y} = {result}")
                times = 0
                break
            else:
                continue
        
print(f"Score: {score}")