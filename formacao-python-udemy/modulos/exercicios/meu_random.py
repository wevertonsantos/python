from random import randrange
def get_random_lista(inicial, final, tam):
    lista = []
    for i in (0,tam):
        lista.append(randrange(inicial,final))
    return lista

print(get_random_lista(100,200,4))