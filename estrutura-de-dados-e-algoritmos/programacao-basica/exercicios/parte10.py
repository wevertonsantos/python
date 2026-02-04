'''

Crie uma classe chamada aluno com os seguintes atributos:
- Nome
- Nota 1
- Nota 2
- Crie um construtor para a classe (__init__)



Crie as seguintes funções (métodos):
- Calcula média, retornando a média aritmética entre as notas
- Mostra dados, que somente imprime o valor de todos os atributos
- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

Crie dois objetos (aluno1 e aluno2) e teste as funções

'''

class Aluno:
    def __init__(self, nome,nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media
    
    def mostra_dados(self):
        return f'Nome: {self.nome}, nota1: {self.nota1}, nota2: {self.nota2} e média: {self.media}'
    
    def verifica_aprovacao(self):
        if self.media >= 6.0:
            return 'Aprovado'
        else:
            return 'Reprovado'

aluno1 = Aluno('Weverton',5,5)
print(aluno1.calcula_media())
print(aluno1.mostra_dados())
print(aluno1.verifica_aprovacao())

aluno2 = Aluno('Lucas',10,5)
print(aluno2.calcula_media())
print(aluno2.mostra_dados())
print(aluno2.verifica_aprovacao())