def main():
    word = input("Input: ").strip()
    print(shorten(word))

def shorten(word=""):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for vowel in vowels:
        if vowel in word:
            word = word.replace(vowel,"")
    return f"Output: {word}"

if __name__ == "__main__":
    main()