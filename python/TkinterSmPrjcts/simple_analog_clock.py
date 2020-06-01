import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.title("Analog Clock")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(width = 3)


# Creating a function to draw a clock

def draw_clock(hr, mnt, sec, pen):
    
    
    #Draw Clock Face
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")    
    pen.pendown()
    pen.circle(210)
    
    
    #Draw the lines for the hours
    pen.up()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range (12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        
    #Draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (hr/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
    
    #Draw the minutes hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (mnt/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)
    
    #Draw the seconds hand
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (sec/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(160)


#we are going to import th time module up in the import section

while True:
    hr = int(time.strftime("%I"))
    mnt = int(time.strftime("%M"))
    sec = int(time.strftime("%s"))
    draw_clock(hr, mnt, sec, pen)
    wn.update()
    time.sleep(1)
    
    pen.clear()








wn.mainloop()