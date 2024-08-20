#https://cs50.harvard.edu/python/2022/psets/1/interpreter/

def main():
    expression = input("Expression: ").strip()
    print(math(expression))

def math(expression):
    datas = []
    for exp in expression:
        if exp != " ":
            if exp != "+" and exp != "-" and exp != "*" and exp != "/":
                exp = int(exp)
                datas.append(exp)
            else:
                datas.append(exp)

    if "+" in datas:
        return add(datas)
    elif "-" in datas:
        return subtract(datas)
    elif "*" in datas:
       return multiply(datas)
    else:
        return divide(datas)

def add(datas):
    x = datas[0]
    z = datas[2]
    return f"{x + z:.1f}"

def subtract(datas):
    x = datas[0]
    z = datas[2]
    return f"{x - z:.1f}"

def multiply(datas):
    x = datas[0]
    z = datas[2]
    return f"{x * z:.1f}"

def divide(datas):
    x = datas[0]
    z = datas[2]
    return f"{x / z:.1f}"

main()