try:
    text = input('Enter something: ')
except EOFError:
    print('EOF interrupt')
except KeyboardInterrupt:
    print('Keyboard interrupt')
else:
    print(text)