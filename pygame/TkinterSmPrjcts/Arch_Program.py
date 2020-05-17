import turtle

arch = turtle.Pen()
for i in range(6):
    first_side = input()   
    dist = int(first_side)
    arch.forward(dist)
    print("Add Object")
    Object = input()
    if Object is "door":
        arch.up()
        dist = int(input())
        arch.forward(dist)        
    else:
        arch.down()
        dist = int(input())
        arch.forward(dist)        
       
