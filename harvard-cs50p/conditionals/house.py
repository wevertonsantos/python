name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # | == or
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #"_" significa qualquer outra coisa
        print("Who?")