from tkinter import *
import random
import time

#Screen_Size
WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Animations")
canvas.pack()

class Ball:
        def __init__(self, size, color):
                
                self.shape = canvas.create_oval(0, 0, size, 2*size, fill = color)
                self.xspeed = random.randrange(1, 45)
                self.yspeed = random.randrange(1, 45)
                        
        def move(self):
                canvas.move(self.shape, self.xspeed, self.yspeed)
                pos = canvas.coords(self.shape)
                #print(pos)
                if pos[1] <= 0 or pos[3] >= HEIGHT:
                     self.yspeed = -self.yspeed
		
                elif pos[0] <= 0 or pos[2] >= WIDTH:
                      self.xspeed = -self.xspeed

colors = ["blue","red","green", "gold", "purple", "turquoise", "pink", "silver", "grey"]


balls = []
for i in range(random.randrange(10, 20)):
    balls.append(Ball(random.randrange(20, 80),random.choice(colors)))
    #print(i)
    
while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.02)



tk.mainloop()
