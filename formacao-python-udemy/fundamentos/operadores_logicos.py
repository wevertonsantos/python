'''
and - resulta verdadeiro se todos os valores envolvidos na operação forem verdadeiros, caso contrário resulta false

or - resulta em verdadeiro se qualquer um dos operadores for verdadeiro

not - inverte o resultado lógico

Not(True) = False
Not(False) = True
'''

# usando and

resultado1 = True and False
print(resultado1)

resultado2 = True and True
print(resultado2)

var1 = True
var2 = False
var3 = False
print(var1 and var2 and var3)

clima_bom = True
estou_disposto = True
vou_ao_mercado = clima_bom and estou_disposto
print(vou_ao_mercado)