#https://cs50.harvard.edu/python/2022/psets/2/plates/

def main():
    plate = input("Plate: ")
    print("Valid") if is_valid(plate) else print("Invalid")

def is_valid(s):
    ...

s = "CS50"
if len(s) == 6 or len(s) > 2:
    for i in range(len(s)):
        #se placa começa com duas letras
        if i < 2:
            if not s[i].isnumeric():
                print("Invalid")
                if len(s) % 2 == 0:
                    len_str = len(s) / 2
                else:
                    len_str = len_str(s)
else:
    print("Invalid")

main()