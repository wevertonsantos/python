def main():
    x = int(input("What's x? "))
    print(f"{x} is Even") if is_even(x) else print(f"{x} is Odd")        

def is_even(n):
    return True if n % 2 == 0 else False
    
main()