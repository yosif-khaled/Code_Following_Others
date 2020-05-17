#this tut was actually in python 2.7

import turtle
import time
import random
import os
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")
#wn.bgpic("images.gif") ## to import a picture
wn.setup(width = 600, height = 600)
wn.tracer(0)

#draw border:
pen = turtle.Turtle()
pen.penup()
pen.goto(-290, -290) #similar to .setposition()
pen.pendown()
pen.pensize(3)
pen.color("gold")
for side in range (4):
    pen.forward(580)
    pen.left(90)
pen.hideturtle()


#create player turtle
#when turtle is created it will always be looking right
player = turtle.Turtle()
player.color("black")
player.shape("turtle")
player.penup()
player.speed(0)

#creating collectables

max_collectable_no = 6
collectables = []

for count in range(max_collectable_no):
    collectables.append(turtle.Turtle())
    collectables[count].shape("circle")
    collectables[count].color("blue")
    collectables[count].penup()
    collectables[count].speed(0)
    collectables[count].setposition(random.randint(-240, 240), random.randint(-240, 240))

#setting speed
## play with speed
player_speed = 1
collectable_speed = 1
#score
score = 0


#define turning functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global player_speed
    player_speed += 1
def decreasespeed():
    global player_speed
    player_speed -= 1


def is_collision(t1, t2):
    #d is the distance from the center betn 2 objects
    d = math.sqrt(math.pow((t1.xcor() - t2.xcor()), 2) +  math.pow((t1.ycor() - t2.ycor()), 2))
    if d < 20:
        return True
    else:
        return False



#setting keboard bindings

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")




while True:
    
    ##
    #for sound on collisions
    #import os (already imported)
    #add os.system("aplay //afplay for mac filename.extension&")
    #the & at the end is just to make it play without to stop everything alse
    ##
    
    wn.update()
    player.forward(player_speed)

    #boundry check (collisions with walls)
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    elif player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        
    for count in range(max_collectable_no):
        
            #Collectable motion
        collectables[count].forward(collectable_speed)
    
        ##
        # commented code is acting funny if done later should
        # have a separate function
        # two conditionals one for the negative value -280
        # and the other is the one written down below
        ##
        
        if collectables[count].xcor() > 290 or collectables[count].xcor() < -290:
            #collectable.setposition(280, collectable.ycor())
            collectables[count].right(random.randint(180, 240))
        elif collectables[count].ycor() > 290 or collectables[count].ycor() < -290:
            #collectable.setposition(collectable.xcor(), 280)
            collectables[count].right(random.randint(180,240))

        #Collision
        if is_collision(player, collectables[count]):
            collectables[count].goto(random.randint(-270, 270), random.randint(-270, 270))
            collectables[count].right(random.randint(0, 360))
            score += 1
            pen.undo()
            pen.color("black")
            pen.up()
            pen.hideturtle()
            pen.goto(310, 310)
            str_score = "Score: %s" %score
            pen.write(str_score, align = "left", font = ("Ariel", 14, "normal"))
            








wn.mainloop()