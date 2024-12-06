#https://cs50.harvard.edu/python/2022/psets/6/lines/
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif '.py' not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1]) as file:
            print(file)

main()