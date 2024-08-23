#https://cs50.harvard.edu/python/2022/psets/2/camel/

def main():
    name = input("camelCase: ")
    print(camel_case(name))

def camel_case(name):
    ...

main()

name = "caMelCase"
for _ in name:
    ...
if name == name.capitalize():
    print()