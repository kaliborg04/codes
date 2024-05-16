players = {}
while True:
    player = input('Enter player: ')
    if len(player) == 0:
        break

    num_goals = 0
    while True:
        goals = input("Enter goals: ")
        if goals.isdigit():
            num_goals = int(goals)
            if num_goals > 0:
                break
            print("Error: goals must be > 0")
        else:
            print("Error: goals must be a number")
    
    if player in players:
        players[player] += num_goals
    else:
        players[player] = num_goals
print(players)
