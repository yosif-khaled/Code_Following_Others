for i in range(4):
	name = input("what's your name?")
	print("Hello, ", name)
	age = input("How old are you? ")
	print("next year you will be ", int(age)+1)
	if int(age) < 6:
		print("You can't handle this ride")
	elif int(age) >= 6 and int(age) < 14:
		print("you are just the right age")
	else:
		print("you are an old creeposorus")