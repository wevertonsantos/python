class Lista:
    def __init__(self):
        pass

    def __enter__(self):
        print("Memória iniciada")
        self.lista = []
        return self.lista

    def __exit__(self,*args,**kwargs):
        print("Memória liberada")
        del self.lista

with Lista() as temp_lista: # iniciando objeto com with
    print(temp_lista)