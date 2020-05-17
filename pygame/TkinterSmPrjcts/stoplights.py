import turtle
import random
import time

wn = turtle.Screen()
wn.title("Stoplights")
wn.bgcolor("black")

#drawing the stoplight box
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.up()
pen.goto(-30,60)
pen.down()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)


# red light

red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0,40)


# yellow light

yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0,0)


# green light

green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0,-40)

while True:
    yellow_light.color("grey")
    red_light.color("red")
    time.sleep(2)
    red_light.color("grey")
    green_light.color("green")
    time.sleep(2)
    green_light.color("grey")
    yellow_light.color("yellow")
    time.sleep(2)
    
    
wn.mainloop() #to keep the window open