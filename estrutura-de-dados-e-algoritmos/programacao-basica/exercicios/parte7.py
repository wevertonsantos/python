'''

Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
- ValueError: se o usuário digitar um caracter
- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
- KeyboardInterrupt: caso o usuário interrompa a execução

'''

lista = []
try:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    lista.append(valor1)
    lista.append(valor2)
    
    divisao = lista[0] / lista[1]
except ValueError:
    print("Você digitou um valor inválido")
except ZeroDivisionError:
    print("Você tentou fazer divisão por zero")
except IndexError:
    print("Não existe esse índice na lista")
except KeyboardInterrupt:
    print("Usuário interrompeu a execução")
else:
    print(f"A divisão é: {divisao}")