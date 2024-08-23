#https://cs50.harvard.edu/python/2022/psets/1/interpreter/

def main():
    expression = input("Expression: ").strip()
    if " " in expression:
        print(math(expression))
    else:
        print("Enter a valid expression")

def math(expression):
    datas = expression.split(" ")

    if "+" in datas:
        return add(datas)
    elif "-" in datas:
        return subtract(datas)
    elif "*" in datas:
        return multiply(datas)
    else:
        return divide(datas)

def add(datas):
    x = int(datas[0])
    z = int(datas[2])
    return f"{x + z:.1f}"

def subtract(datas):
    x = int(datas[0])
    z = int(datas[2])
    return f"{x - z:.1f}"

def multiply(datas):
    x = int(datas[0])
    z = int(datas[2])
    return f"{x * z:.1f}"

def divide(datas):
    x = int(datas[0])
    z = int(datas[2])
    return f"{x / z:.1f}"

main()

#pegar o valor antes do +
#pegar o valor depois do +
#somar os valores se conter o +
math = input("")
datas = math.split(" ")
x = int(datas[0])
z = int(datas[2])
print(x - z)