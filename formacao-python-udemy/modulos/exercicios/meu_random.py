from random import randrange
def get_random_lista(inicial, final, tam):
    lista = []
    i = 0
    while i < tam:
        lista.append(randrange(inicial,final))
        i += 1
    return lista