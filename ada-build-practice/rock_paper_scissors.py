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

import random

def choose_rps():
  r = random.randint(0,2) #returns random number 0 to 2
  
  if r == 0:
      return "rock" # 0 = rock
  elif r == 1:
      return "scissors" # 1 = scissors
  else:
      return "paper" # 2 = paper

def rps_function(player1, player2):
  # tie
  if player1 == player2:
    print("It's a tie!")
  # player1 = scissors
  elif player1 == "scissors":
    if player2 == "rock":
      print ("Player 2 won!")
    else:
      print("Player 1 won!")
    # player1 = rock
  elif player1 == "rock":
    if player2 == "scissors":
      print ("Player 1 won!")
    else:
      print("Player 2 won!")
  # player1 = paper
  else:
    if player2 == "scissors":
      print ("Player 2 won!")
    else:
      print("Player 1 won!")
       

def play_again():
  r = random.randint(0,1)
  if r == 0:
    return True
  else:
    return False

play = True

print("Welcome to Rock, Paper, Scissors!\n")
while play == True:
  player1 = choose_rps()
  player2 = choose_rps()

  print("Player 1 chose", player1, ".")
  print("Player 2 chose", player2, ".")

  rps_function(player1, player2)

  print(" ")

  play = play_again()

print("Thank you for playing!") 