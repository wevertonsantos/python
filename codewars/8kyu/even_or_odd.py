# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(x):
    if x % 2 != 0:
        return "Odd"
    else:
        return "Even"