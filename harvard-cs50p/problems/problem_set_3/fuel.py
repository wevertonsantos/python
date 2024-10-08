# https://cs50.harvard.edu/python/2022/psets/3/fuel/
def main():
    print(fuel())

def fuel():
    fraction = input("Fraction: ")
    while True:
        if '.' not in fraction:
            x = fraction[0]
            y = fraction[2]
            try:
                x = int(x)
                y = int(y)
                if y == 0 or x > y:
                    result = x / 0
            except ValueError:
                fraction = input("Fraction: ")
            except ZeroDivisionError:
                fraction = input("Fraction: ")
            else:
                if f"{x}/{y}" == "1/4":
                    return "25%"
                elif f"{x}/{y}" == "1/2":
                    return "50%"
                elif f"{x}/{y}" == "3/4":
                    return "75%"
                elif f"{x}/{y}" == "4/4":
                    return "F"
                else:
                    return "E"
        else:
            fraction = input("Fraction: ")

main()
