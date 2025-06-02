numero = 11
if numero < 10:
    print("Menor que 10")
elif numero < 100:
    print("Menor que 100")
elif numero <= 1000:
    print("Menor ou igual a 1000")
else:
    print("Nenhuma anterior")

texto = 's'
if texto == 'a':
    print("É vogal")
elif texto == 'e':
    print("É vogal")
elif texto == 'i':
    print("É vogal")
elif texto == 'o':
    print("É vogal")
elif texto == 'u':
    print("É vogal")
else:
    print("É consoante")

#if ternário
numero = 10
resultado = "Esse número é par" if numero % 2 == 0 else "Esse número é impar"
print(resultado)

numero = 3
resultado = "Um" if numero == 1 else "Dois" if numero == 2 else "Três"