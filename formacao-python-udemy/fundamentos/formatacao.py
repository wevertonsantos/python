# Formatação de texto

'''
%s para texto
%d para inteiro
%f para ponto flutuante
'''

nome = "Carolina"
texto_formatado = "O nome dela é %s" % (nome)
print(texto_formatado)

nome = "Rodrigo"
idade = 23
altura = 1.73
texto = "Meu nome é %s. Tenho %d anos e tenho %f m de altura" % (nome,idade,altura)
print(texto)