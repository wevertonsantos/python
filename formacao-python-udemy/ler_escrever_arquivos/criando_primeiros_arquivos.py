arquivo = open("exemplo.txt","wt") # "w" abre um arquivo para escrita, se não existir o arquivo é criado/ "t" abre um arquivo em modo texto
arquivo.write("Olá estou escrevendo no arquivo\n") # escrevendo uma linha no arquivo
arquivo.write("Está é a segunda linha do arquivo")
arquivo.close() # fecha o arquivo

lista = ["Ana","Fernando","João","Maria"]
arquivo = open("nomes.txt","wt")
for item in lista:
    arquivo.write(item + '\n')
arquivo.close()

texto = ["Ana\nMaria\nFernando"]
arquivo = open("nomes2.txt","wt")
arquivo.writelines(texto) #writelines para escrever texto no arquivo ao invés de linha por linha 
arquivo.close()

lista = [str(i) + '\n' for i in range(0,20)]
arquivo = open('numeros_3.txt','wt')
arquivo.writelines(lista)
arquivo.close()