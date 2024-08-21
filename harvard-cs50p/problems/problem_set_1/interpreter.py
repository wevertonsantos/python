#https://cs50.harvard.edu/python/2022/psets/1/interpreter/

def main():
    expression = input("Expression: ").strip()
    if " " in expression:
        print(math(expression))
    else:
        print("Enter a valid expression")

def math(expression):
    datas = []
    arr_expression = expression.split(" ")
    if len(arr_expression) == 3:
        for data in arr_expression:
            if data != " ":
                if data != "+" and data != "-" and data != "*" and data != "/":
                        data = int(data)
                        datas.append(data)
                else:
                    datas.append(data)
    else:
        return "Enter a valid expression"

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