#https://cs50.harvard.edu/python/2022/psets/2/coke/

#Se a soma das coins que o user inseriu não é da quantia do valor da garrafa, o valor devido deve chegar até ser igual a 0

amount_due = 50
coin = 0
while amount_due != 0:
    print(f"Amount Due: {amount_due}")
    coin = input("Insert Coin: ")
    if coin.isdigit():
        coin = int(coin)
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
        else:
            print("Enter a valid coin")
            break
    else:
        print("Enter a integer")
        break
else:
    print(f"Change Owed: {amount_due}")