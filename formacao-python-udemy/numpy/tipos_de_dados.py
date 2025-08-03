import numpy

boolean = numpy.bool_(True) # criando variável do tipo numpy booleana
print(boolean,type(boolean))

string = numpy.bytes_("este e um texto") # criando variável do tipo numpy bytes
print(string)

string = numpy.str_("este é um texto") # criando variável do tipo numpy string
print(string)

inteiro = numpy.intc(-10) # criando variável inteiro que ocupa 32 bits
print(inteiro)

uinteiro = numpy.uintc(102) # criando variável inteiro sem sinal