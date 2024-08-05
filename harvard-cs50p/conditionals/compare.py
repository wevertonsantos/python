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
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")

'''
or : ou
and : e
'''

if x < y or x > y: #or
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")

if x != y: #diferente
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")

if x == y: #comparação
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")