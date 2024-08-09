'''
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
'''

#1 - State the problem clearly. Identify the input & output formats.
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3
def locate_test(cards,query):
    pass

#2 - Come up with some example inputs & outputs. Try to cover all edge cases.
test = { #representando o teste e como deve retornar/se comportar referente aos dados passados
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

#Fazendo testes para verificação
res = locate_test(cards,query) == output
print(res)
res = locate_test(**test['input']) == test['output']
print(res)

tests = []
tests.append(test)
tests.append({
    'input': {
        'cards': [1, 11, 5, 7, 32, 3, 1, 0],
        'query': 32
    },
    'output': 4
})

tests.append({
    'input': {
        'cards': [-23, 11, -5, 7, 32, 3, 1, 0],
        'query': -23
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [-8, 11, -23, 7, 12, 4, 2, 0],
        'query': 900
    },
    'output': -1
})

#We will assume that our function will return -1 in case cards does not contain query
def locate_card(cards,query):
    for i in range(len(cards)):
        if cards.__contains__(query):
            if cards.index(query) == i:
                return i
        else: return -1

#efetuando testes
cards = tests[0]['input']['cards']
print(locate_card(cards,7)) # return 3

cards = tests[1]['input']['cards']
print(locate_card(cards,32)) #return 4

cards = tests[2]['input']['cards']
print(locate_card(cards,-23)) #return 0

cards = tests[3]['input']['cards']
print(locate_card(cards,900)) #return -1