#imports
import turtle
import random

wn = turtle.Screen()
wn.title("Fall n' Catch")
wn.bgcolor("green")
wn.setup(width = 800, height = 600)
wn.tracer(0)

score = 0
lives = 3

# add player
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, -250)

# create item list
items = []
# add item
for _ in range(10):
    item = turtle.Turtle()
    item.shape("circle")
    item.color("blue")
    item.penup()
    item.speed(0)
    items.append(item)
    item_speed = random.randint(1, 5)
    item.setpos(random.randint(-380, 380), 300)
    
# create enemy list
enemies = []
# add enemies
for _ in range(10):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    enemies.append(enemy)
    enemy_speed = random.randint(1, 5)
    enemy.setpos(random.randint(-380, 380), 300)
    
    
   
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 260)
pen.write("Score: {} Lives: {}".format(score, lives), align = "center", font = ("Courier", 24, "normal"))

# variables
x = player.xcor()


def go_left():
    global x
    x -= 5
    player.setx(x)
    
def go_right():
    global x
    x += 5
    player.setx(x) 


# this function causes a proplem when used in a while loop
#def item_motion():
    #global y
    #y -= 1
    #item.sety(y)
    #if y < -300:
        #item.setpos(0, 300)
    # can be done in one line
    #item.sety(item.ycor() -= 1)
    




wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()
    
    for item in items:
        # item motion    
        y = item.ycor()
        y -= item_speed
        item.sety(y)
        # can be done in one line
        #item.sety(item.ycor() -= 1)
        
        # off screen check
        
        if y < -300:
            item.setpos(random.randint(-380, 380), 300)
        
        # check for collision
        
        if item.distance(player) < 20:
            item.setpos(random.randint(-380, 380), 300)
            score += 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align = "center", font = ("Courier", 24, "normal"))
            
    for enemy in enemies:

        y = enemy.ycor()
        y -= enemy_speed
        enemy.sety(y)
        
        if y < -300:
            enemy.setpos(random.randint(-380, 380), 300)
        
        # check for collision
        
        if enemy.distance(player) < 20:
            enemy.setpos(random.randint(-380, 380), 300)
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align = "center", font = ("Courier", 24, "normal"))


wn.mainloop()

## Spaghetti code will return and fix it later
## add .gifs using wn.register_shape
## and you know how to add sound