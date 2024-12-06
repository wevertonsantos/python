#https://cs50.harvard.edu/python/2022/psets/6/lines/
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif '.py' not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        try:
            lines = []
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.startswith("\n") and not line.startswith("'''") and "#" not in line:
                       lines.append(line)
                print(len(lines))
        except FileNotFoundError:
             sys.exit("File does not exist")

main()