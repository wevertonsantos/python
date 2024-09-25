#https://cs50.harvard.edu/python/2022/psets/4/adieu/
import inflect
p = inflect.engine()

def main():
    list_names = []
    try:
        while True:
            name = input("Name: ").strip()
            list_names.append(name)
    except KeyboardInterrupt:
        output = "Adieu, adieu, to " + p.join((list_names))
        print(output)

main()