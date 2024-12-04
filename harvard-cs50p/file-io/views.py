import csv
from PIL import Image

def main():
    with open("views.csv","r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id"])

main()