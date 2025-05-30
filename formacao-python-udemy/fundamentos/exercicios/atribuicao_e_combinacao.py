# 1 - Crie um programa que responda se você foi aprovado numa prova. 
# Você somente foi aprovado numa prova se sua média for maior ou igual que 7 
# ou se sua nota no exame for maior ou igual a 5. Leia esses valores por input.

media = int(input("Digite sua média: "))
nota_exame = int(input("Digite sua nota do exame: "))
verifica_aprovacao = (media >= 7) or (nota_exame >= 5)
print("Aprovado:", verifica_aprovacao)

# 2 - Crie  um programa que diga se a senha esta correta e portanto você tem 
# acesso ao sistema. A senha devera ser salva no código, e a tentativa deve ser 
# lida por input.

senha = "2434"
senha_input = input("Digite a senha: ")
verificacao_senha = senha == senha_input
print("Acesso ao sistema:",verificacao_senha)