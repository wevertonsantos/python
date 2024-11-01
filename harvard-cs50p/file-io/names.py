names = []
for _ in range(3):
    names.append(input("What's your name? "))
print(names)

file = open("names.txt","w")
for name in names:
    if name == names[-1]:
        file.write(f"{name}")
    else:
        file.write(f"{name}\n")
file.close