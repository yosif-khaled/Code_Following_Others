import turtle

HEXAGON = 8
PENTAGON = 6
SQUARE = 4
TRIANGLE = 3

def draw_shape(shape):
	if shape == "Square":
		for i in range(0,4):
			turtle.forward(50)
			turtle.left(90)
	if shape == "Triangle":
		for i in range(0,3):
			turtle.forward(50)
			turtle.left((180/3)*2)
	turtle.fd(100)


turtle.goto(-250, 0)

for i in range(0, 2):
	draw_shape("Square")
	draw_shape("Triangle")

#why did he use this function
delay = input("Press Enter to Finish...")
