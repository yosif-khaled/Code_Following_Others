#2-players(Human-Computer)
	#playermoves
	#computermoves
	#comparemoves
import random

moves = ["r","p","s"]
win_moves = ["pr","sp","rs"]
cpu = 0
hum = 0
while True:
	player_move = input("What is your move:  ")
	computer_move = random.choice(moves)
	outcome = player_move + computer_move
	print(outcome)
	if player_move == "quit":
		break
	elif computer_move == player_move:
		print("Tie")
	elif outcome in win_moves:
		print("You WIn")
		hum += 1
	else:
		print("You Lose")
		cpu += 1
	print("Your Score is: ", hum , "\nCpu Score is : " , cpu)
