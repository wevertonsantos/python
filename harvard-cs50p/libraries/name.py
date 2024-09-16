#https://docs.python.org/3/library/sys.html

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

print("hello, my name is", sys.argv[0], sys.argv[1])