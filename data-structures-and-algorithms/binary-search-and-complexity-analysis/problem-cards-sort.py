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

#9,7,6,4,3,2,1

def locate_cards(cards,query):
    #precisa verificar o elemento do meio
    element_middle = (len(cards) - 1) / 2
    for i in range(len(cards)):
        #se é igual a query
        print(i)

locate_cards(cards,6)