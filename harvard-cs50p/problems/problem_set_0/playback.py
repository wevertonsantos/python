def main():
    speak = input()
    print(playback(speak))

def playback(speak):
    speak = speak.replace(" ", "...")
    return speak

main()