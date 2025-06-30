numero = 70
caractere = chr(numero) # Conversão de número para caractere
print("O número %d é mapeado para o caractere '%s'" % (numero,caractere))

for i in range(32,100):
    caractere = chr(i)
    print("O número %d é mapeado para o caractere '%s'" % (i,caractere))

caractere = 'F'
numero = ord(caractere) # Conversão de caractere para número
print("O caractere %s é mapeado para o número %d" % (caractere,numero))