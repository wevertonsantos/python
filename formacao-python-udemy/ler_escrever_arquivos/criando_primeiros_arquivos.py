arquivo = open("exemplo.txt","wt") # "w" abre um arquivo para escrita, se não existir o arquivo é criado/ "t" abre um arquivo em modo texto
arquivo.write("Olá estou escrevendo no arquivo\n") # escrevendo uma linha no arquivo
arquivo.write("Está é a segunda linha do arquivo")
arquivo.close() # fecha o arquivo