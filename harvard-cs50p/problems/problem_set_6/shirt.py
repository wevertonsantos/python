#https://cs50.harvard.edu/python/2022/psets/6/shirt/
import sys
from PIL import Image

def main():
    if verify_arg():
        #with Image.open(sys.argv[1]) as input, open(sys.argv[2]) as output:
        print("pass")

def verify_arg(): 
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line-arguments")
    elif sys.argv[1].count(".") != 1 or sys.argv[2].count(".") != 1:
        sys.exit("Invalid input")
    elif "." in sys.argv[1] and sys.argv[1].count(".") == 1 and "." in sys.argv[2] and sys.argv[2].count(".") == 1:
        if ".jpg" not in sys.argv[1] and ".jpeg" not in sys.argv[1] and ".png" not in sys.argv[1]:
            sys.exit("Invalid input")
        elif ".jpg" not in sys.argv[2] and ".jpeg" not in sys.argv[2] and ".png" not in sys.argv[2]:
            sys.exit("Invalid input")
        elif not sys.argv[1][sys.argv[1].index("."):] == sys.argv[2][sys.argv[2].index("."):]:  
            sys.exit("Input and output have different extensions")
        else:
            return True

main()