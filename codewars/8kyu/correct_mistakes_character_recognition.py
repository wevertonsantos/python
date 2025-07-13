'''
https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python

8 kyu
Correct the mistakes of the character recognition software
'''
s = "51NGAP0RE"
def correct(s):
    return s.replace("5","S").replace("0","O").replace("1","I")
print(correct(s))