from tkinter import *
import random
import time

WIDTH = 1024
HEIGHT = 960

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
canvas.pack()
tk.title("Animations")



class Shape:
    def __init__(self, size_x, size_y, color):
        
        self.shapes = [canvas.create_rectangle(0, 0, size_x, size_y, fill = color),
                      canvas.create_oval(0, 0, size_x, size_y, fill = color)]
        self.shape = random.choice(self.shapes)
        self.speed_x = random.randrange(10, 20)
        self.speed_y = random.randrange(10, 20)



    def move(self):
        canvas.move(self.shape, self.speed_x, self.speed_y)
        pos = canvas.coords(self.shape)
        
        if pos[0] <= 0 or pos[2] >= WIDTH:
            self.speed_x = - self.speed_x
        elif pos[1] <= 0 or pos[3] >= HEIGHT:
            self.speed_y = - self.speed_y



colors = ['red' ,'blue' ,'green' ,'gold' ,'black']
shapes = []

for i in range(4):
    shapes.append(Shape(random.randrange(10, 45), random.randrange(20, 45), random.choice(colors)))
    print(i)

while True:
    for shape in shapes:
        shape.move()
    tk.update()
    time.sleep(0.02)

tk.mainloop()
