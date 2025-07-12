'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
'''

prices = [7,1,5,3,6,4]

for price in prices:
    menor_preco = []
    if min(prices) == price:
        menor_preco.append(price)