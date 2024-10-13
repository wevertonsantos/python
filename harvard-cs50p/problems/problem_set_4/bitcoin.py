#https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import sys
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()

try:
    bitcoins = float(sys.argv[1])
    usd = o['bpi']['USD']['rate_float']
    converted = bitcoins * usd
    output = f"${converted:,}"
    print(output)
except requests.RequestException:
    sys.exit("Missing command-line argument")