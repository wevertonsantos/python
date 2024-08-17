#https://cs50.harvard.edu/python/2022/psets/1/deep/

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(result(answer))

def result(answer):
    answer = answer.lower().strip()
    return "Yes" if answer == str(42) or answer == "forty-two" or answer == "forty two" else "No"

main()