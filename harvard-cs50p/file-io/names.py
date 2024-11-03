'''
name = input("What's your name? ")

file = open("names.txt","a")
file.write(f"{name}")
file.close
'''

'''
with open("names.txt","r") as file: #working "with" with file
    for line in file:
        print(f"Hello, {line.rstrip()}")
'''

'''
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("Hello",name)
'''

with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")