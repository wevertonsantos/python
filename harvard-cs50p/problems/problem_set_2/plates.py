#https://cs50.harvard.edu/python/2022/psets/2/plates/

def main():
    plate = input("Plate: ").strip()
    print("Valid") if is_valid(plate) else print("Invalid")

def is_valid(s):
    if len(s) == 6 or len(s) > 2:
        numbers = []
        if invalid_things(s) == False:
            for i in range(len(s)):
                if s[i].isnumeric(): numbers.append(s[i])
                if i < 2:
                    if s[i].isnumeric():
                        return False
                elif not s[-1].isnumeric():
                    return False
                elif not numbers == []: 
                    if int(numbers[0]) == 0:
                        return False
            else:
                return True
        else:
            return False
    else:
        return False

def invalid_things(s):
    invalid_things = [".",";",":"," ","!",",","?"]
    while True:
        for invalid_thing in invalid_things:
            if invalid_thing in s:
                return True
            else:
                continue
        return False

main()