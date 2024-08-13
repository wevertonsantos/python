# i é 0
for i in [0,1,2]:
    print("au")
    
#caso não for usar a  variável depois
for _ in range(3):
    print("hey")

#concatenar string * n
print("au " * 3)
print("au\n" * 3, end="") # nada bom

while True:
    n = int(input("What's n? "))
    if n > 0:
       break

for _ in range(n):
    print("au")