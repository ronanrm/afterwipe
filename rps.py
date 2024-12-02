player_1 = []
player_2 = []
P1_wins = 0
ties = 0
P2_wins = 0
def test_rps(player_1, player_2):
    player_1 = str(input("Player 1, enter: rock, paper, or scissors: "))
    player_2 = str(input("Player 2, enter: rock, paper, or scissors: "))    
    if player_1 == 'rock' and player_2 == 'scissors' or player_1 == 'scissors' and player_2 == 'paper' or player_1 == 'paper' and player_2 == 'rock':
        P1_wins += 1
        return ("Player 1 is the winner")
    if player_1 == player_2:
        ties += 1
        return ('tie')
    else:
        P2_wins += 1 # counter doesn't work
        return ("Player 2 wins")
peter = test_rps(player_1, player_2)
print(peter)
print("Player 1 has ", P1_wins,"wins, Player 2 has ", P2_wins," wins. There have been ", ties,"ties.")
