import numpy

boolean = numpy.bool_(True) # criando variável do tipo numpy booleana
print(boolean,type(boolean))

string = numpy.bytes_("este e um texto") # criando variável do tipo numpy bytes
print(string)

string = numpy.str_("este é um texto") # criando variável do tipo numpy string
print(string)

inteiro = numpy.intc(-10) # criando variável inteiro que ocupa 32 bits
print(inteiro)

uinteiro = numpy.uintc(102) # criando variável inteiro 32 bits sem sinal

#inteiro de 64 bits
long = numpy.int_(8328832)

#inteiro de 64 bits sem sinal
ulong = numpy.uint(2020203)

#ponto flutuante 64 bits
ponto_flutuante = numpy.float64(1000.23)

#ponto flutuante 32 bits
ponto_flutuante2 = numpy.float32(4993.32)

#ponto flutuante 16bits
ponto_flutuante3 = numpy.float16(12)

#inteiro de 8 bits
int8 = numpy.int8(20)

#inteiro de 16 bits
int16 = numpy.int16(1000)

# inteiro 8 bits sem sinal
uint8 = numpy.uint8(34)

#inteiro 16 bits sem sinal
uint16 = numpy.uint16(32)

# criação de array
array = numpy.array([1,2,3,4,5,6,7,8,9,0]) 

#passando tipo para array com dtype
array = numpy.array([1,2,3,4,5,6,7,8,9,0],dtype=numpy.int8) 

'''
i = inteiro
b = booleano
u = inteiro sem sinal
f = ponto flutuante
S = string (bytes)
U = texto unicode
'''

array = numpy.array(["abc","def","ghi"],dtype='S3') #passando string com 3 bytes de tamanho
print(array.itemsize) # número de bytes por item
print(array.nbytes) # dizer o total de bytes nesta variável

# criando nosso próprio tipo pessoa com dtype
tipo_pessoa = numpy.dtype([('nome','S10'),('idade','i4')])
#passando nosso tipo criado para o array.
array = numpy.array([('Rodrigo',24)],dtype=tipo_pessoa)