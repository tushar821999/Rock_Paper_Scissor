# rules for winner rock paper and scissors
# 1. Rock blunts Scissors
# 2. Paper covers rock
# 3. Scissors cut paper
from random import randint
# this is for the player
print("****************************************")
player_name = input("Player 1 Name : ")
print("")
print("Player Name : ",player_name)
print("Computer Name : Frost")
print("****************************************")
print("")
player = input('rock (r) , paper (p) , scissors (s) : ')
print(player,"vs ",end='')
# this is for the computer name = Frost
chosen = randint(1,3)
if chosen == 1:
	computer = 'r'
elif chosen == 2:
	computer = 'p'
else:
	computer = 's'

print(computer)
# lets code who are win

if player == computer:
	print("DRAW ! ")
elif player == 'r' and computer == 's':
	print(player_name," wins !")
elif player == 'r' and computer == 'p':
	print("Frost wins !")
elif player == 'p' and computer == 'r':
	print(player_name," wins !")
elif player == 'p' and computer == 's':
	print("Forst wins !")
elif player == 's' and computer == 'p':
	print(player_name," wins !")
elif player == 's' and computer == 'r':
	print("Frost wins")
print("****************************************")
print("")
print("Developed By Tushar Verma")





