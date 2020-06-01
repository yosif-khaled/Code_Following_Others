import turtle

fred = turtle.Pen()
fred.shape("turtle")
fred.speed(10)
for i in range (1000):
	fred.circle(180)
	fred.backward(i + 4)
	fred.left(45)
	fred.forward(i - 2)
