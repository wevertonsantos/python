# python suporta (+ = * / %)
x = int(input("What's x? ")) #variável tipo inteiro
y = int(input("What's y? "))
print(x + y)

a = float(input("What's a? ")) #variável tipo float
b = float(input("What's b? "))
c = round(a + b) #https://docs.python.org/3/library/functions.html#round
print(f"{c:,}") #formatando float para adicionar (.) a milhar

d = round(a / b, 2) # aredondando com duas casas decimais
print(d)
d = a / b
print(f"{d:.2f}") # aredondando com duas casas decimais