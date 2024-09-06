def main():
    height = int(input("Height:"))
    pyramid(height)

def pyramid(n):
    for i in range(n + 1):
        print("#" * i)

main()