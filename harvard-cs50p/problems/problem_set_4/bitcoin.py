#https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import sys
import requests

bitcoins = sys.argv[1]
try:
    bitcoins = float(bitcoins)
except requests.RequestException:
    sys.exit("Missing command-line argument")