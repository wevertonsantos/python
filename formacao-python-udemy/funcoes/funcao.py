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

def len_int(num):
    numero_em_texto = str(num)
    return len(numero_em_texto)

num1 = 10
num2 = 1234
tamanho1 = len_int(num1)
tamanho2 = len_int(num2)
print("O número %d tem %d dígitos" % (num1,tamanho1))
print("O número %d tem %d dígitos" % (num2,tamanho2))

# Retornar muitos valores em uma função (vira uma tupla)
def retorna_multiplo():
    return 1,2

valor = retorna_multiplo()
print(valor)

# Atribuindo valores para cada variável
x,y = retorna_multiplo()
print(x,y)

# Função Lambda
soma = lambda x : x + 10 # Função anônima e simples
valor = soma(10)
print(valor)

# Função lambda com mais de uma parâmetro/argumento
multiplica = lambda x,y : x * y
valor = multiplica(10,5)
print(valor)

# Função normal retornando função lambda
def multiplica(y):
    return lambda x : x * y

valor = multiplica(2)
print(valor(10))

# Funções recursivas
def print_num(num):
    print(num)
    if num >= 10:
        return # return para encerrar
    print_num(num + 1) # chamando a função e add + 1

print_num(0)

def print_str(texto,indice):
    if indice == len(texto):
        return
    print(texto[indice])
    print_str(texto, indice + 1)

print_str("Olá",0)

def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)

print(fatorial(5))

# Funções aninhadas (quando tem uma segunda função declarada dentro de outra função)

def pai():
    def filho():
        print("sou filho")
    filho()

pai()

def calculadora(x,y,op):
    def soma(a,b):
        return a + b
    def subtrai(a,b):
        return a - b
    if op == '+':
        return soma(x,y)
    elif op == '-':
        return subtrai(x,y)
    
print(calculadora(10,10,'+'))
print(calculadora(10,5,'-'))

def pega_func_print():
    def print_var(var):
        print(var)
    return print_var
 
print_me = pega_func_print() # Criando instância de uma função
print_me(10)

# Decorators
def Maiusculo(func):
    def inner_func():
        return func().upper()
    return inner_func

@Maiusculo # Utilizando decorator
def retorna_string():
    return "string de teste"

valor = retorna_string()
print(valor)

def Minusculo(func):
    def inner_func(st1,str2):
        return func(st1,str2).lower()
    return inner_func

@Minusculo # Utilizando decorator
def retorna_strings(str1,str2):
    return str1 + str2

valor = retorna_strings("OLÁ ","MUNDO")
print(valor)