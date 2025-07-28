with open("exemplo_with.txt",'wt') as arquivo: # nessa abordagem com with não é preciso fechar porque ele vai criar e fechar com with
    arquivo.write("Olá")

# abrir arquivo que foi gerado
arquivo = open("exemplo.txt","rt") # r - abre um arquivo para leitura, se não existir ele gera exceção.
lido = arquivo.read() # lendo todo o arquivo com read()