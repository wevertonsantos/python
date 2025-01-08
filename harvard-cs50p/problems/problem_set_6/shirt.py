#https://cs50.harvard.edu/python/2022/psets/6/shirt/
import sys

def main():
    if verify_arg():
        print("ok")

def verify_arg():
    if len(sys.argv) == 1: sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2: sys.exit("Too many command line-arguments")
    else: return True

main()