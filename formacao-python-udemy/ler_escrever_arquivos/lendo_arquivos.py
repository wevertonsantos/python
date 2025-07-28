with open("exemplo_with.txt",'wt') as arquivo: # nessa abordagem com with não é preciso fechar porque ele vai criar e fechar com with
    arquivo.write("Olá")