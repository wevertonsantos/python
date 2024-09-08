#https://cs50.harvard.edu/python/2022/psets/3/taqueria/

def main():
    item = input("Item: ").strip().title()
    cost = 0
    while True:
        try:
            for product in menu:
                if item == product:
                    price = float(menu[product])
                    cost += price
                    print(f"$ {cost:.2f}")
                    item = input("Item: ").strip().title()
            if item == '':
                item = int(item)
            else:
                item = input("Item: ").strip().title()
        except ValueError:
            exit()

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()