#https://cs50.harvard.edu/python/2022/psets/4/figlet/
import sys
from pyfiglet import Figlet
import random

def main():
    f = ""
    if len(sys.argv) == 1:
        s = input("Input: ").strip()
        font_random = random.choice(['slant','fuzzy'])
        f = Figlet(font_random)
        print(f.renderText(s))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            s = input("Input: ").strip()
            f = Figlet(sys.argv[2])
            print(f.renderText(s))
        else:
            sys.exit
    else:
        sys.exit()

main()