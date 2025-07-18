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

try:
    print(lista[0])
except:
    print("Falha ao acessar")
else: # else executado somente se não houver erro
    print("Não houve erro")

try:
    divisao = 10 / 0
    print(lista[10])
except IndexError as error_index: # tipo de sessão específica do python (tipo de erro index erro)
    print("Erro de acesso ao índice:",str(error_index))
except ZeroDivisionError as error_zero_divisao: # tipo de erro para divisão por zero
    print("Erro de divisão por zero:",str(error_zero_divisao))

def printa_positivo(num):
    if num < 0:
        raise ValueError("Valor não pode ser negativo") # lançando um erro criado pelo programador
    print(num)

try:
    printa_positivo(-1)
except ValueError as erro:
    print("O erro é:",str(erro))

def print_positivo(num):
    assert(num >= 0) # criando outra exceção se o teste lógico der falso
    print(num)

try:
    print_positivo(-1)
except AssertionError as erro:
    print("O erro é:",str(erro))