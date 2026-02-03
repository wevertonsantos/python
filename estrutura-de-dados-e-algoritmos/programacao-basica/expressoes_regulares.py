'''
Metacaracteres:

. - qualquer caractere (exceto linha nova)
\w - qualquer caractere alfanumérico
\W - qualquer caractere não-alfanumérico
\d - qualquer caractere que seja um dígito (0-9)
\D - qualquer caractere não dígito
\s - espaço em branco
^ - começa com
$ - termina com
\ - usado antes de metacaracteres para especificar seu significado literal

Quantificadores - permitem determinar como e quantas vezes os metacaracteres aparecem

[] - opcional entre os que estão dentro dos colchetes
() - captura grupos de caracteres
* - de zero a mais vezes
? - zero ou uma vez
+ - uma ou mais vezes
{m,n} - de m a n vezes
| - ou
'''

# re - regular expression
import re

#função search - primeiro ocorrência que aparece em um texto
frase = 'Olá, meu número de telefone é (42)00000-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}',frase))

frase = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
print(re.search('[A-Za-z]{3}-\d{4}',frase))

email = 'Entre em contato, meu email é teste@teste.com'
print(re.search('\w+@\w+\.com',email))

#função match - indicar se uma expressão regular está no início do texto

frase = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
print(re.match('[A-Za-z]{3}-\d{4}',frase))

frase2 = 'FRT-1998 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}',frase2))

#função findall - encontrar várias ocorrências

frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}',frase3))

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''
print(re.findall('\w+@\w+\.\w+',emails))