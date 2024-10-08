'''
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).
'''

def count_by(x,n):
    array = []
    for i in range(1,n + 1): array.append(i*x)
    return array

x_in_n = count_by(2, 5)
print(x_in_n)