#https://cs50.harvard.edu/python/2022/psets/6/pizza/
import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif '.csv' not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                rows = []
                reader = csv.DictReader(file)
                any(append_rows(row,rows) for row in reader)
                print(grid(sys.argv[1],rows))
        except FileNotFoundError:
            sys.exit("File does not exist")

def append_rows(row,list):
    ''' Adding rows within list '''
    if sys.argv[1] == "sicilian.csv":
        list.append([row["Sicilian Pizza"], row["Small"], row["Large"]])
    elif sys.argv[1] == "regular.csv":
        list.append([row["Regular Pizza"], row["Small"], row["Large"]])

def grid(argv,rows):
    ''' Returning table as grid '''
    if argv == "sicilian.csv":
        return tabulate(rows,["Sicilian Pizza","Small","Large"],"grid")
    elif argv == "regular.csv":
        return tabulate(rows,["Regular Pizza","Small","Large"],"grid")

main()