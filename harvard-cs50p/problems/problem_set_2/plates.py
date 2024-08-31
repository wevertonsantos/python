#https://cs50.harvard.edu/python/2022/psets/2/plates/

def main():
    plate = input("Plate: ")
    print("Valid") if is_valid(plate) else print("Invalid")

def is_valid(s):
    ...

s = "AAA222"
sum_str = 0
middle_element = 0

def invalid_things(s):
    invalid_things = [".",";"," ","!",",","?"]
    for invalid_thing in invalid_things:
        return False if invalid_thing not in s else True
index = int()
ads = s[int(len(s) / 3)]
if len(s) == 6 or len(s) > 2:
    numbers = []
    if invalid_things(s) == False:
        for i in range(len(s)):
            if s[i].isnumeric(): numbers.append(s[i])
            if i < 2:
                if s[i].isnumeric():
                    print("Invalid")
                    break
            elif s[int(len(s) / 3)].isnumeric():
                print("Invalid")
                break
            elif not numbers == []: 
                if int(numbers[0]) == 0:
                    print("Invalid")
                    break
            else:
                print("Invalid")
                break
        else:
            print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

#main()