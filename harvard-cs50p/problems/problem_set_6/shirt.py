#https://cs50.harvard.edu/python/2022/psets/6/shirt/
import sys
from PIL import Image

def main():
    if verify_arg():
        with Image.open(sys.argv[1]) as input, open(sys.argv[2]) as output:
            ...

def verify_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line-arguments")
    else:
        return

main()