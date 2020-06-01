from tkinter import *
import random
import time

WIDTH = [1024, 800, 640]
HEIGHT = [960, 600, 480]
width = 0
height = 0

resolution_of_choice = input("pick a resolution:\n1) 1024*960\n2) 800*600\n3) 640*480\n")
if resolution_of_choice == '1':
	width = WIDTH[0]
	height = HEIGHT[0]
elif resolution_of_choice == '2':
	width = WIDTH[1]
	height = HEIGHT[1]
elif resolution_of_choice == '3':
	width = WIDTH[2]
	height = HEIGHT[2]
else:
	print("write down your resolution:")
	width = input("WIDTH: ")
	height = input("HEIGHT: ")
	


tk = Tk()

canvas = Canvas(tk, width = width, height = height)
tk.title("Creating More Animation")

canvas.pack()

class Ball:
	
	def __init__(self):
		colors_available = ["red", "orange", "green", "blue", "purple", "black", "brown"]
		self.color = random.choice(colors_available)
		self.size = random.randrange(20, 100)
		self.shape = canvas.create_oval(0, 0, self.size, self.size, fill = self.color)
		#the self.speed only works if placed here, I don't know why??
		#if I placed it outside the __init__ it doesn't work?!
		self.x_speed = random.randrange(1, 8)
		self.y_speed = random.randrange(1, 8)
		
	def Move(self):
		
		canvas.move(self.shape, self.x_speed, self.y_speed)
		pos = canvas.coords(self.shape)
		#print(pos)
		if pos[1] <= 0 or pos [3] >= height:
			self.y_speed = - self.y_speed
		
		elif pos[0] <= 0 or pos[2] >= width:
			self.x_speed = - self.x_speed

		

newball = Ball()


while True:
	newball.Move()
	tk.update()
	time.sleep(0.01)
	

tk.mainloop()
