i = 3
while i != 0:# 3 é diferente de 0?
    print("meow")#printa
    i -= 1# 3 - 1 = 2
    # 0 é diferente de 0? não, é igual, então para

i = 0
while i < 3:
    print("rss")
    i += 1

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()