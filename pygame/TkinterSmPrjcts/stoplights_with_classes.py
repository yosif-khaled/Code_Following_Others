import turtle
import random
import time

wn = turtle.Screen()
wn.title("Stoplights")
wn.bgcolor("black")

class Stoplight():
    def __init__(self, x, y):
        self.pen = turtle.Turtle()
        self.pen.color("blue")
        self.pen.width(3)
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.up()
        self.pen.goto(x - 30, y + 60)
        self.pen.down()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        
        self.color = ""

        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()

        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)
        
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        
        self.red_light.shape("circle")
        self.yellow_light.shape("circle")
        self.green_light.shape("circle")
        
        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()
        
        self.red_light.goto(x, y + 40)
        self.yellow_light.goto(x, y)
        self.green_light.goto(x, y - 40)
        
    def change_color(self, color):
        
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        if color == "red":
            self.red_light.color("red")
            self.color = "red"
        elif color == "yellow":
            self.yellow_light.color("yellow")
            self.color = "yellow"
        elif color == "green":
            self.green_light.color("green")
            self.color = "green"            

    def timer(self):
        if self.color == "red":
            self.change_color("green")
            wn.ontimer(self.timer, 2000)
        elif self.color == "yellow":
            self.change_color("red")
            wn.ontimer(self.timer, 2000)
        elif self.color == "green":
            self.change_color("yellow")
            wn.ontimer(self.timer, 2000)
            
            
        
stoplight0 = Stoplight(0, 0)
stoplight0.change_color("red")
stoplight0.timer()

stoplight1 = Stoplight(100, 0)
stoplight1.change_color("yellow")
stoplight1.timer()

stoplight2 = Stoplight(-100, 0)
stoplight2.change_color("green")
stoplight2.timer()





wn.mainloop() #to keep the window open