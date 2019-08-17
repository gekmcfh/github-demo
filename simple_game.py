#simple game
#demonstrates importing modules

import games,random

print("Welcome to most simple game in the world!")
again = None

while again is not "n":
    players = []
    num = games.ask_number(question = "How many players are involved? (2-5)",low=2,high=5)

    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100)+1
        player = games.Player(name, score)
        players.append(player)

    print("\nHere game results:")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nDo you wanna play again? (y/n): ")

input("Press any key to exit. ")