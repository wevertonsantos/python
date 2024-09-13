#https://cs50.harvard.edu/python/2022/psets/3/grocery/

def main():
    list_items = []
    list_shopping = []
    while True:
        try:
            product = input()
            list_items.append(product)
        except KeyboardInterrupt:
            for item in list_items:
                if [item,list_items.count(item)] not in list_shopping:
                    list_shopping.append([item,list_items.count(item)])
            list_shopping.sort()
            for values in list_shopping:
                print(values[1],values[0].upper())
            exit()

main()