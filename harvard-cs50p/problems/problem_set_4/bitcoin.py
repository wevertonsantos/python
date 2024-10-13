#https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import sys
import requests

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
    except requests.RequestException:
        ...
    bitcoins = check_argv()
    bitcoins_to_usd(o,bitcoins)

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

def bitcoins_to_usd(o,bitcoins):
    usd = o['bpi']['USD']['rate_float']
    converted = bitcoins * usd
    output = f"${converted:,}"
    return print(output)

main()