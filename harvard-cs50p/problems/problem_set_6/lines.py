#https://cs50.harvard.edu/python/2022/psets/6/lines/
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        if '.py' not in sys.argv[1]:
            sys.exit("Not a Python file")

main()