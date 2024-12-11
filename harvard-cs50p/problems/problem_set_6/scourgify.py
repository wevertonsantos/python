#https://cs50.harvard.edu/python/2022/psets/6/scourgify/
import csv
import sys

def main():
    if len(sys.argv) < 3: sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3: sys.exit("Too many command-line arguments")
    elif '.csv' not in sys.argv[1]: sys.exit("Not a CSV File")
    else:
        try:
            with open(sys.argv[1],"r") as input, open(sys.argv[2],"w") as output:
                reader = csv.DictReader(input)
                writer = csv.DictWriter(output,fieldnames=["first","last","house"])
                writer.writeheader()
                for row in reader:
                    name = row["name"]
                    first_last = name.split(",")
                    house = row["house"]
                    writer.writerow({"first":first_last[0],"last":first_last[1].strip(),"house":house})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

main()