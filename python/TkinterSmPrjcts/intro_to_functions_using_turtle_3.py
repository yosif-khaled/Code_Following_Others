import turtle

def draw_shape(shape, color):
	#forgot to add the color function
	turtle.color(color)
	if shape == "Square":
		for i in range(0,4):
			turtle.fd(50)
			turtle.lt(90)
		turtle.fd(80)
	elif shape == "Triangle":
		for i in range(0,3):
			turtle.fd(50)
			turtle.lt(360/3)
		turtle.fd(50)

turtle.goto(0, 0)

draw_shape("Square", "Blue")
draw_shape("Triangle", "red")

delay = input("Press Enter To Terminate >>>")
