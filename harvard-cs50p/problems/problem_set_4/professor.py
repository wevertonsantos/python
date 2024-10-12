#https://cs50.harvard.edu/python/2022/psets/4/professor/
import random

def main():
    level = get_level()
    integer = generate_integer(level)
    problems = []
    while True:
        x = random.randint(1,integer)
        y = random.randint(1,integer)
        problems.append([x,y])
        if len(problems) == 10:
            break
    print(score(problems))

def get_level():
    while True:
        level = input("Level: ")
        if level.isnumeric():
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                return level

def generate_integer(level):
    if level == 1:
        integer = random.randint(1,9)
    elif level == 2:
        integer = random.randint(1,99)
    else:
        integer = random.randint(1,999)
    return integer

def score(problems):
    times = 0
    score = 0
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
    return f"Score: {score}"

if __name__ == "__main__":
    main()