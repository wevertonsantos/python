#https://pypi.org/project/cowsay/
import cowsay
import sys
from sayings import hello #import module

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    #cowsay.cow("hello, " + sys.argv[1])
    hello(sys.argv[1])