'''

Para revisar o conteúdo prático sobre expressões regulares, implemente o exercício abaixo. Logo em seguida você pode acessar a aula em vídeo com a solução

Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
- Números
- CEPs
- URLs

'''
import re

texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"

print(re.findall('\d',texto))
print(re.findall('\d{5}-\d{3}',texto))
print(re.findall('https?://[A-Za-z0-9./]+',texto))