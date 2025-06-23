def func(): # Bloco de código reutilizável
    num = 10
    print("Uma função %d " % num)

func() # Chamando a função

# Função que não faz nada com pass
def func():
    pass

# Função que tem parâmetro
def var(numero):
    print(numero)

var(2)

# Função com mais parâmetros
def soma(x,y):
    print("A soma dos números é: %.2f" % (x + y))

soma(10,20)

# Função com parâmetro arbitrário
def func(*args):
    print(type(args))
    print("Argumentos são:",args)

func()

# Função com parâmetro arbitrário e outro normal
def func(*args, par):
    print(args)
    print(par)

func(1,2,3, par="1")
func(par='1')

# Função com argumentos arbitrários
def func(valor,nome = "Teste"): # Atribuindo variável padrão
    print(valor,nome)

func(3)
func(3, "Outro nome") # Também podemos atribuir novo nome na variável padrão

# Função com parâmetros que tem nome e tamanho arbitrário
def func(**args): # O args vira um dicionário
    print(type(args))
    print(args)
    print(args['valor'])

func(valor = '10', operacao = 'Soma', resultado = 10)

# Função com parâmetro com outra função
def printing(x):
    print(x)

def execute(func,x):
    func(x)

funcao = printing
print(type(funcao))
execute(printing,'Olá')

# Função que retorna valores
def subtrai(x,y):
    valor = x - y
    return valor

subtracao = subtrai(10,3)
print(subtracao)