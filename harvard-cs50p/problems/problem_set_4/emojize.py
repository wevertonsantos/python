#https://cs50.harvard.edu/python/2022/psets/4/emojize/
import emoji

def main():
    s = input("Input: ").strip()
    print(f"Output: {emoji.emojize(s, language='alias')}")

main()