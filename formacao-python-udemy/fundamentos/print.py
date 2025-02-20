# Gerando saídas com python
print("Olá mundo!")
print(10)
print(20.5)
print('olá mundo') # utilizando aspas simples

# Para imprimir vários valores
print("Maçã",20,30.45)

# Print com separador
print("Maçã","Pera","Uva", sep=" - ")
print("Maçã","Pera","Uva", sep=".")

# Determinando end para print
print("Maçã","Pera", end=" Fim",sep=" ")

# Quebrando linha com \n
print("Este é um texto longo,","e preciso que quebre a linha",sep="\n")

# Adicionando variáveis no print e declarando ela
print("A pontuação total de %s foi de %s pontos" % ("Fernando","10"))

# Usando variáveis com format no print
print("A pontuação total de {} foi de {} pontos".format("Fernando","10"))

# Concatenação com print
print("A pontuação total de " + "Fernando " + "foi de " + "10 " + "pontos")