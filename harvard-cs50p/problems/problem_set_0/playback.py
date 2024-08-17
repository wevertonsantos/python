#https://cs50.harvard.edu/python/2022/psets/0/playback/

def main():
    speak = input()
    print(playback(speak))

def playback(speak):
    speak = speak.replace(" ", "...")
    return speak

main()