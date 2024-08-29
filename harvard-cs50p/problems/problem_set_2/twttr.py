#https://cs50.harvard.edu/python/2022/psets/2/twttr/

def main():
    text = input("Input: ").strip()
    print(omitting_vowels(text))

def omitting_vowels(text):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for vowel in vowels:
        if vowel in text:
            text = text.replace(vowel,"")
    return f"Output: {text}"

main()