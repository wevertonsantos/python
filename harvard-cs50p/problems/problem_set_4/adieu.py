#https://cs50.harvard.edu/python/2022/psets/4/adieu/

def main():
    list_names = []
    try:
        while True:
            name = input("Name: ").strip()
            list_names.append(name)
    except KeyboardInterrupt:
        output = "Adieu, adieu, to "
        last_name = list_names[-1]
        first_name = list_names[0]
        if len(list_names) == 1:
            output += name
        elif len(list_names) == 2:
            output += f"{first_name} and {last_name}"
        else:
            for one_name in list_names:
                if one_name != last_name:
                    output += f"{one_name}, "
            output += f"and {last_name}"
        print(output)

main()