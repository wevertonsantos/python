#https://cs50.harvard.edu/python/2022/psets/1/interpreter/

def main():
    expression = input("Expression: ").strip()
    print(math(expression))

def math(expression):
    datas = []
    for data in expression.split(" "):
        if data != " ":
            if data != "+" and data != "-" and data != "*" and data != "/":
                data = int(data)
                datas.append(data)
            else:
                datas.append(data)

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