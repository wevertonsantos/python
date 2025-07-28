with open("exemplo_with.txt",'wt') as arquivo: # nessa abordagem com with não é preciso fechar porque ele vai criar e fechar com with
    arquivo.write("Olá")

# abrir arquivo que foi gerado
arquivo = open("exemplo.txt","rt") # r - abre um arquivo para leitura, se não existir ele gera exceção.
lido = arquivo.read() # lendo todo o arquivo com read()
arquivo.close()

arquivo = open("exemplo.txt","rt")
primeira_linha = arquivo.readline() # ler linha
segunda_linha = arquivo.readline()
print(primeira_linha)
print(segunda_linha)
arquivo.close()

#percorrendo arquivo por laço
arquivo = open("exemplo.txt","rt")
for linha in arquivo:
    print(linha)
arquivo.close()