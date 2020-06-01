import turtle

HEXAGON = 8
PENTAGON = 6
SQUARE = 4
TRIANGLE = 3

def draw_square():
	for i in range(0, 4):
		turtle.forward(50)
		turtle.left(90)
	turtle.forward(100)
def draw_triangle():
	for i in range(0,3):
		turtle.forward(50)
		turtle.left(360/3)
	turtle.forward(80)

draw_square()
draw_triangle()

#why did he use this function
delay = input("Press Enter to Finish...")
