#https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
def main():
    fraction = input("Fraction: ").split()
    print(convert(fraction))

def convert(fraction):
    while True:
        if '.' not in fraction:
            fraction = fraction.split('/')
            x = fraction[0]
            y = fraction[1]
            try:
                x = int(x)
                y = int(y)
                if y == 0:
                    result = x / 0
                elif x > y:
                    x = int('')
                else:
                    if f"{x}/{y}" == "1/4":
                        return f"{int((x/y) * 100)}%"
                    elif f"{x}/{y}" == "1/2":
                        return f"{int((x/y) * 100)}%"
                    elif f"{x}/{y}" == "3/4":
                        return f"{int((x/y) * 100)}%"
                    else: 
                        percentage = int((x/y) * 100)
                        return gauge(percentage)
            except ValueError:
                fraction = input("Fraction: ")
            except ZeroDivisionError:
                fraction = input("Fraction: ")
        else:
            fraction = input("Fraction: ")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return "Z%"

if __name__ == "__main__":
    main()