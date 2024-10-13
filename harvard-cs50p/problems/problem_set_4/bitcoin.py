#https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import sys
import requests

try:
    bitcoins = float(sys.argv[1])
except requests.RequestException:
    sys.exit("Missing command-line argument")