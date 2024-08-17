#https://cs50.harvard.edu/python/2022/psets/1/bank/

def main():
    greeting = input("Greeting: ").strip().lower()
    print(check_greeting(greeting))

def check_greeting(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

main()