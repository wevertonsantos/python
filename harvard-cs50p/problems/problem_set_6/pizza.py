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
                sicilian = []
                regular = []
                reader = csv.DictReader(file)
                for row in reader:
                    if sys.argv[1] == "sicilian.csv":
                        sicilian.append([row["Sicilian Pizza"], row["Small"], row["Large"]])
                    elif sys.argv[1] == "regular.csv":
                        regular.append([row["Regular Pizza"], row["Small"], row["Large"]])
                if sys.argv[1] == "sicilian.csv":
                    print(tabulate(sicilian,["Sicilian Pizza","Small","Large"],"grid"))
                elif sys.argv[1] == "regular.csv":
                    print(tabulate(regular,["Sicilian Pizza","Small","Large"],"grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")

main()