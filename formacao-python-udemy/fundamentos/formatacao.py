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
texto = "Meu nome é %s. Tenho %d anos e tenho %.2f m de altura" % (nome,idade,altura)
print(texto)

# Formatando ponto flutuante
numero_gigante = 1.123456789
print("Número gigante formatado: %.2f" % numero_gigante)

# Formatando valor booleano
valor = True
print("O valor é: %s" % (valor))
print("O valor é: %d" % (valor))

# Formatando decimal para inteiro
decimal = 23.33
print("A parte inteira é: %d" % (decimal))

# Formatação com caracteres especiais
texto = "Quebrando\nlinha e colocando\n\ttabulação"
print(texto)

texto = "Deixa a \"palavra\" entre aspas" # Caracter literal
print(texto)