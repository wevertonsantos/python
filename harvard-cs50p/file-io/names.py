'''
name = input("What's your name? ")

file = open("names.txt","a")
file.write(f"{name}")
file.close
'''

with open("names.txt","r") as file: #working "with" with file
    lines = file.readlines() #reading lines

for line in lines:
    print(f"Hello, {line.rstrip()}")