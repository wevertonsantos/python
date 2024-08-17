#https://cs50.harvard.edu/python/2022/psets/1/bank/

def main():
    greeting = input("Greeting: ").strip().lower()
    check_greeting(greeting)

def check_greeting(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()