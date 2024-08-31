#https://cs50.harvard.edu/python/2022/psets/2/plates/

def main():
    plate = input("Plate: ")
    print("Valid") if is_valid(plate) else print("Invalid")

def is_valid(s):
    ...

s = "AAA222"
sum_str = 0
middle_element = 0
if len(s) == 6 or len(s) > 2:
    for i in range(len(s)):
        #se placa começa com duas letras
        if i < 2:
            if s[i].isnumeric():
                print("Invalid")
                break
        elif middle_element:
            if len(s) % 2 != 0:
                sum_str += i
                middle_element = sum_str / len(s)
                if not middle_element.is_integer():
                    print("Invalid")
                else:
                    print("Valid")
            

else:
    print("Invalid")

#main()

'''
if not middle_element.is_integer():
    print("Invalid")
else:
    print("Valid")
'''