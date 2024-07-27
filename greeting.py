def saudar(input):
    if input in "hello" or "hey":
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = saudar("oi")
print(greeting)