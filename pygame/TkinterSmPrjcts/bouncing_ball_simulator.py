#this one was difficult for me
#because I am not comfortable using the turtle module

import turtle
import random

#setting up the screen

window = turtle.Screen()

window.bgcolor("black")
window.title("Bouncing Ball Simulator")
window.tracer(0) #stops the screen from updating

balls = []

for _ in range(10):
	balls.append(turtle.Turtle())
	
colors = ["green", "blue", "red", "yellow", "purple", "gold"]
shapes = ["circle", "square", "triangle"]
##ball
for ball in balls:

	#ball = turtle.Turtle() this line creates a new turtle that's why we deleted it because we are already creating and appending to tha alls list
	ball.shape(random.choice(shapes))
	ball.color(random.choice(colors))
	ball.penup()
	ball.speed(2)
	x = random.randint(-290, 290)
	y = random.randint(200,400)
	ball.goto(x, y)
	##keep track of change in x and y
	ball.dy = 0
	ball.dx = random.randint(-1,1)
	ball.da = random.randint(-2,2)

gravity = 0.01

while True:
	window.update()

	for ball in balls:
		ball.rt(ball.da)
		ball.dy -= gravity
		ball.sety(ball.ycor() + ball.dy)

		ball.setx(ball.xcor() + ball.dx)
		#check for wall collision
		if ball.xcor() > 300:
			ball.dx *= -1
		if ball.xcor() < -300:
			ball.dx *= -1
			ball.da *= -1

		#check for a bounce
		if ball.ycor() < -200:
			ball.dy *= -1
			ball.da *= -1

window.mainloop()
