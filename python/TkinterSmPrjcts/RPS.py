#computer pick a random number
#player makes a guess
#compare guess to number
#print out answer
import random
secret = random.randrange(1, 101)
#print(secret)
guess = 0
tries = 0
while guess != secret:
	guess = int(input('enter your guess: '))
	tries = tries + 1
	if guess == secret:
		print("You are Right")
	elif guess < secret:
		print("You answer is too low")
	elif guess > secret:
		print("your answer is too high")

print("The number of tries is ",tries)
