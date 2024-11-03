'''
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

students = []

with open("students.cs") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name,"house":house}
        students.append(student)

def get_name(student):
    return student['name']

for student in sorted(students,key=get_name): #passing function to sorted by name
    print(f"{student['name']} is in {student['house']}")