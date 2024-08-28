#https://cs50.harvard.edu/python/2022/psets/2/coke/

amount_due = 50
coin = 0
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = input("Insert Coin: ")
    if coin.isdigit():
        coin = int(coin)
        if coin == 25 or coin == 10 or coin == 5:
                if coin < amount_due:
                    amount_due -= coin
                else:
                     amount_due = coin - amount_due
                     print(f"Change Owed: {amount_due}")
                     break
        else:
            print(f"Amount Due: {amount_due}")
            break
    else:
        print("Enter a positive integer")
        break
else:
    print(f"Change Owed: {amount_due}")