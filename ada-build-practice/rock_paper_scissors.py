# Rock, Paper, Scissors Project

# Is player1 === player2?
# Yes -> tie
# No -> continue
# Is player1 rock?
    # Yes -> Is player2 scissors?
        # Yes -> player1 won
        # No ->  player2 won
    # No -> continue
# Is player1 paper?
    # Yes -> Is player2 rock?
        # Yes -> player1 won
        # No ->  player2 won
    # No -> continue
# Is player1 scissors?
    # Yes -> Is player2 paper?
        # Yes -> player1 won
        # No ->  player2 won

def rps(player1, player2):

if player1 == player2:
    print('It\'s a tie!')
elif player1 == "rock":
    if player2 == "scissors":
        print('Player 1 won!')
    else:
        print('Player 2 won!')
elif player1 == "paper":
    if player2 == "rock":
        print('Player 1 won!')
    else:
        print('Player 2 won!')
elif player1 == "scissors":
    if player2 == "paper":
        print('Player 1 won!')
    else:
         print('Player 2 won!')

rps('rock', 'paper')