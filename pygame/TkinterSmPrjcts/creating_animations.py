from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = Tk()

canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Drawing")
canvas.pack()

ball = canvas.create_oval(10,10,60,60, fill = "orange")

xspeed = 1
yspeed = 2

while True:
	canvas.move(ball, xspeed, yspeed)
	pos = canvas.coords(ball)
	if pos[1] <= 0 or pos [3] >= HEIGHT:
		yspeed = -yspeed
		
	elif pos[0] <= 0 or pos[2] >= WIDTH:
		xspeed = -xspeed
	
	tk.update()
	time.sleep(0.01)

tk.mainloop()
