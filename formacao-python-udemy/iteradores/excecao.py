lista = [1,2,3]
iterador = iter(lista)
while True:
    try:
        print(next(iterador)) # vai fazer a interação
    except:
        break # se não houver mais vai gerar exceção