#https://cs50.harvard.edu/python/2022/psets/4/figlet/
import sys
from pyfiglet import Figlet
import random

def main():
    fonts = Figlet.getFonts(Figlet())
    if len(sys.argv) == 1:
        s = input("Input: ").strip()
        random_font = random.choice(fonts)
        f = Figlet(random_font)
        print(f"Output: \n {f.renderText(s)}")
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            s = input("Input: ").strip()
            f = Figlet(sys.argv[2])
            print(f"Output: \n {f.renderText(s)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()