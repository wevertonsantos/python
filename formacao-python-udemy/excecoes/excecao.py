lista = [1,2,3]
try: # tentando fazer a ação
    print(lista[10])
except Exception as error: # irá ser executado caso apresente o erro
    print("Falha ao acessar. Mensagem:", str(error)) # mostrando mensagem original da exceção com Exception

try:
    print(lista[10])
except:
    print("Falha ao acessar")
finally: # finally irá executar de qualquer forma
    print("Executa sempre que o try-except acabar")