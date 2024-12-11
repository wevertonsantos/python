#https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import csv
import sys

def main():
    if len(sys.argv[1]) == 1: sys.exit("Too few command-line arguments")
    elif len(sys.argv[1]) > 2: sys.exit("Too many command-line arguments")
    elif '.csv' not in sys.argv[1]: sys.exit("Not a CSV File")
    else:
        try:
            ...
        except FileNotFoundError:
            sys.exit("Could not read [sys.argv[1]]")

main()