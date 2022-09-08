#!/bin/python3
from random import randint
player = input("pick rock, paper, scissor to start the game")
computerchoice = randint(1, 3)
if computerchoice == 1:
  computer = "rock"
elif computerchoice == 2:
  computer = "paper"
else:
  computer = "scissor"

print(player, "vs", computer)

if player == computer:
  print("TIE!")

#checking rock stuff
elif player == 'rock' and computer == 'scissor':
  print("Player wins!")
elif player == 'rock' and computer == 'paper':
  print("Computer wins!")

#checking paper stuff
elif player == 'paper' and computer == 'rock':
  print("Player wins!")
elif player == 'paper' and computer == 'scissor':
  print("Computer wins!")

#checking scissor stuff
elif player == 'scissor' and computer == 'paper':
  print("Player wins!")
elif player == 'scissor' and computer == 'rock':
  print("Computer wins!")
