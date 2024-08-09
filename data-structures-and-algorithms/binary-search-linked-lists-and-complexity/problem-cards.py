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

tests.append({
    'input': {
        'cards': [-8, 11, -23, 7, 12, 4, 2, 0],
        'query': 0
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [6, 6, 6, 7, 7, 4, 4, 4,6,6],
        'query': 7
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [50],
        'query': 50
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

#We will assume that our function will return -1 in case cards does not contain query
def locate_card(cards,query):
    for i in range(len(cards)):
        if cards.__contains__(query): #caso contém query
            if cards.index(query) == i:
                return i
        else: return -1

# query occurs in the middle
cards = tests[0]['input']['cards']
print(locate_card(cards,7)) # retorna 3
cards = tests[1]['input']['cards']
print(locate_card(cards,32)) #retorna 4

# query is the first element
cards = tests[2]['input']['cards']
print(locate_card(cards,-23)) #retorna 0

# cards does not contain query 
cards = tests[3]['input']['cards']
print(locate_card(cards,900)) #retorna -1

# query is the last element
cards = tests[4]['input']['cards']
print(locate_card(cards,0)) #retorna 7

# numbers can repeat in cards
cards = tests[5]['input']['cards']
print(locate_card(cards,7)) #retorna 3

# cards contains just one element, query
cards = tests[6]['input']['cards'] #retorna 0
print(locate_card(cards,50))

# cards is empty
cards = tests[7]['input']['cards'] #SOLUCIONAR tem que retornar -1
print(locate_card(cards,7))