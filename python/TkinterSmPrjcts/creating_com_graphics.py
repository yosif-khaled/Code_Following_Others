from tkinter import *
import random

_color = ["blue", "green", "red", "blue", "purple"]
randcolor = random.choice(_color)
#random_color1 = random.choice(_color)
#random_color2 = random.choice(_color)
#random_color3 = random.choice(_color)
#random_color4 = random.choice(_color)
#random_color5 = random.choice(_color)

tk = Tk()
canvas = Canvas(tk, width = 500, height = 400)
tk.title("Drawing")
canvas.pack()

#canvas.create_line( 0, 0, 500, 400, fill = random_color1	)
#canvas.create_rectangle(100, 100, 250, 250, fill = random_color2	)
#canvas.create_oval(20, 20, 55, 55, fill = random_color3	)
#canvas.create_rectangle(300, 300, 450, 400, fill = random_color4	)
#canvas.create_oval(20, 20, 55, 55, fill = random_color5 )

for i in range(10):
	x1 = random.randrange(200)
	x2 = random.randrange(200)
	y1 = random.randrange(200)
	y2 = random.randrange(200)
	randcolor = random.choice(_color)
	canvas.create_rectangle(x1, x2, y1, y2, fill = randcolor)

canvas.mainloop()
