#https://cs50.harvard.edu/python/2022/psets/0/faces/

def main():
    string = str(input("Enter a string with a emoji: "))
    convert(string)

def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return print(string)

main()