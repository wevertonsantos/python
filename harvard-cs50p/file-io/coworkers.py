import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("coworkers.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])