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
list_product = []
item = 0
count_item = 0
while True:
    try:
        item = input()
        list.append(item)
    except KeyboardInterrupt:
        for i in list:
            if [i,list.count(i)] not in list_product:
                list_product.append([i,list.count(i)])
        list_product.sort()
        for list_p in list_product:
            print(list_p[0].upper(),list_p[1])
        exit()

#contando todo item da list ['1','1','1','1']
#na hora de mostrar
#tenho que mostrar o item e a quantidade de item
# '1' 4
#relacionar o item com a quantidade
#main()