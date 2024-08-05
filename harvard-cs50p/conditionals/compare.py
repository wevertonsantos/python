'''
> : maior
>= : maior igual
< : menor
<= : menor igual
== : igual (comparação)
!= : diferente
'''

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print(f"{x} is less than {y}")
if x > y:
    print(f"{x} is greater than {y}")
if x == y:
    print(f"{x} is equal to {y}")