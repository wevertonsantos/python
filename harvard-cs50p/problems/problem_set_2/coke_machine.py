#https://cs50.harvard.edu/python/2022/psets/2/coke/

#Se a soma das coins que o user inseriu não é da quantia do valor da garrafa, mostrar o amontoado, valor devido e fazer com que chegue até o valor devido ser igual a 0

amount_due = 50
coin = 0
while amount_due != 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    amount_due -= coin
else:
    print(f"Change Owed: {amount_due}")