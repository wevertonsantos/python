import os
os.mkdir('pasta') # criando pasta através do os
os.rmdir('pasta') # excluindo pasta (deve estar vazia)

for i in range(0,2):
    nome_pasta = f"pasta_{i}"
    try:
        os.mkdir(nome_pasta)
    except:
        pass

    try:
        open(nome_pasta + '/texto.txt','wt').close()
    except:
        pass


for i in range(0,2):
    nome_pasta = f"pasta_{i}"
    try:
        os.remove(nome_pasta + '/texto.txt')
    except:
        pass

    try:
        os.rmdir(nome_pasta)
    except:
        pass