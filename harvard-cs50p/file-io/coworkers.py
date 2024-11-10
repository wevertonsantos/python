import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("coworkers.csv","a") as file:
    #writer = csv.writer(file)
    #writer.writerow([name,home])
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})