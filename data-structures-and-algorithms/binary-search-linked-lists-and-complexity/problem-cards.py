'''
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
'''

#1 - State the problem clearly. Identify the input & output formats.
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3
def locate_test(cards,query):
    pass

res = locate_test(cards,query) == output
print(res)

#2 - Come up with some example inputs & outputs. Try to cover all edge cases.
test = { #representando a função ou como ela deveria se comportar
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

locate_test(**test['input']) == test['output']

def locate_card(cards,query):
    for i in range(len(cards)):
        if cards.index(query) == i:
            return i