#https://cs50.harvard.edu/python/2022/psets/3/grocery/

def main():
    grocery_list()

def grocery_list():
    list_items = []
    count_item = 0 
    while True:
        items = input()
        list_items.append(items)
        try:
            #escrever a lista e mostrar para item em uppercase com a quantia dolado
            #adicionar o item na lista
            #verificar quantos items tem do mesmo tipo
            for item in list_items:
                count_item = list_items.count(item)
                name_item = item
            print(f"{count_item} {list_items}")
        except EOFError:
            exit()

list = []
list_list = []
count_item = 0
while True:
    item = input()
    list.append(item)
    for item in list:
        print(list[list.index(item)])
        #se a lista já contém o item
        if list.__contains__(item):
            if item in list:
                name_item = item
        else:
            pass
        count_item = list.count(item)
        list_list.append([count_item, name_item])
    print(list_list)

#main()