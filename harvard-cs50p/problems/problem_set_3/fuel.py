#https://cs50.harvard.edu/python/2022/psets/3/fuel/
def main ():
    fraction = input("Fraction: ")
    print(fuel(fraction))

def fuel(fraction):
    while True:
        try:
            x = int(fraction[0])
            y = int(fraction[2])
            if f"{x}/{y}" == "1/4":
                return "25%"
            elif f"{x}/{y}" == "1/2":
                return "50%"
            elif f"{x}/{y}" == "3/4":
                return "75%"
        except ValueError:
            fraction = input("Fraction: ")

main()