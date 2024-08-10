'''
The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called binary search. 

Here's how binary search can be applied to our problem:

Find the middle element of the list.
If it matches queried number, return the middle position as the answer.
If it is less than the queried number, then search the first half of the list
If it is greater than the queried number, then search the second half of the list
If no more elements remain, return -1.
'''
cards = [9,7,6,4,3,2,1]

def locate_cards(cards,query):
    first_half_list = []
    second_half_list = []
    #precisa encontrar o elemento do meio
    element_middle = int((len(cards) - 1) / 2)
    #se o elemento do meio é igual a query
    if element_middle == query:
        #retorna a posição do meio
        return cards[element_middle]
    #se elemento do meio é menor que a query
    elif element_middle < query:
        #procura a primeira parte da lista
        for i in range(0,element_middle):
            first_half_list.append(i)
        if first_half_list[query]:
            ...
    #se elemento do meio for maior que a query
    elif cards[element_middle] > query: # pegar o elemento antes da query
         for i in range(element_middle,len(cards)):
            #procura a secunda parte da lista
            second_half_list.append(i)
            return second_half_list[query]
    else:
         return -1

res = locate_cards(cards,6)
print(res)