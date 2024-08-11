def main():
    difficulty = input("Difficult or Casual? ")
    
    if difficulty == "Difficult" or difficulty == "Casual":
        players = input("Multiplayer or Single-player? ")
        choose(difficulty, players) if players == "Multiplayer" or players == "Single-player" else print("Enter a valid number of players")       
    else:
        print("Enter a valid difficulty")

def choose(difficulty, players):
        if difficulty == "Difficult":
            if players == "Multiplayer":
                recommend("Poker")
            else:
                recommend("Klondike")    
        else:
            if players == "Multiplayer":
                recommend("Hearts")
            else:
                recommend("Clock")

def recommend(game):
    print("You might like", game)

main()