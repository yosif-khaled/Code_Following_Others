import turtle

HEXAGON = 6
PENTAGON = 5
SQUARE = 4
TRIANGLE = 3

def draw_shape(sides, color):
	turtle.color(color)
	
	for i in range(0, sides):
		turtle.fd(50)
		turtle.lt(360/sides)

	turtle.fd(100)

turtle.goto(-250, 0)

draw_shape(3, "blue")
draw_shape(4, "red")
draw_shape(5, "green")
draw_shape(6, "gold")

delay = input("Press Enter To Terminate >>>")