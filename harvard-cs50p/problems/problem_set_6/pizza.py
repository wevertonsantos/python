#https://cs50.harvard.edu/python/2022/psets/6/pizza/
import sys
import csv
import tabulate

def main():
    if sys.argv == 1:
        sys.exit("Too few command-line arguments")
    elif sys.argv > 2:
        sys.exit("Too many command-line arguments")
    elif '.csv' not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                ...
        except FileNotFoundError:
            sys.exit("")

main()