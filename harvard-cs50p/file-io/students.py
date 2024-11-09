import csv

'''
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name,"home":home})
    '''
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name,"house":house}
        students.append(student)
    '''

#def get_name(student):
#    return student['name']

for student in sorted(students,key=lambda student: student["name"]): #passing function to sorted by name
    print(f"{student['name']} is from {student['home']}")