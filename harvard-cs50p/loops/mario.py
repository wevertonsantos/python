def main():
    print_column(3)
    print_row(4)
    print_matriz(3,3)
    print_square(4)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_matriz(width, height):
    for _ in range(height):
        print("?" * width)

def print_square(size):
    #Para cada linha
    for i in range(size):
        #Para cada # na linha
        for j in range(size):
            #Print #
            print("#", end="")
        print()
        

main()