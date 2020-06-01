# christianthompson
import random

#lesson 1&2 printing
print("lesson 1 & 2")
#notice the difference
print("HEllo World")
print("Hello"+"World")
print("Hello","World")
#printing a number as a string vs as an int or float
print("2")
print(2)
print("2"+"2")
print("2","2")
print(2.01 + 3)
#print(2.1 + "2.1") error
print("2.1",2.1)

#lesson 3 string variables
print("lesson 3 string variables")
name = "Robert Smith"
#watch the difference
print(name)
print("name")

#attaching strings to one another
print("name")
print("name: " + name)
print("name: %s" %name)
print("name: {}".format(name))

#basic string methods
print("String Methods")
print("helLo".upper())
print("HELLo".lower())
title = "Sound of Silence"
print(title.capitalize())
print(title.title())

#printing parts of the string, question
#can printed parts be randomized [random.choice]
#because if so it can be used for a video game
#find the treasure online printed messages randomized pieces
#players shoud collaborate to complete the texts they found
#to find the treasure

print("Slices")
print("Good Morning"[0:4])
print("Good Morning"[5:12])
print(title[:5])
print(title[6:8])
print(title[9:])

#experimenting with inputs
##name = input("Write down your name: ")
##if name.lower() == "yosif":
	##print("hello, %s"%name.upper())
#concolusion: conflict of string types is averted in a much easier way

#experimenting with printing text characters
#I need to experiment more with random but the output
#is not what i expected, it is very well organized
#to get the randomized missing words and letters and not in particular order I would have to use char

experiment_letter = "Black and white\nThick and furry\nFast as the wind\nAlways in a hurry\nCouple of spots\nRub my ears\nAlways comes when his name he hears\nLoves his ball; it\'s his favorite thing\nWhat\'s most fun for him? Everything!\nGreat big tongue that licks my face\nHas a crate, his very own space\nBig brown eyes like moon pies\nHe\'s my friend till the very end!"
print(experiment_letter)
print(len(experiment_letter))
length_experiment_letter = len(experiment_letter)
print(length_experiment_letter)
x = random.randrange(0, 339)
print(x)
print(experiment_letter[:x])

#lesson 4 integers and floats
print("Lesson 4 Integers &Floats")

i = 20
x = 6.0
print(i)
print(x)
print(i,x)
print(i+x)
print("i + x")
print(i-x)
print(i*x)
print(i/x)
#modulus %
print(5%4)

#you can't add a string to a float or an int
#print("i = "+ i)
#other words plus sign is for similar types

print("x = %s"%x)
#%s converts the variable to be attached into a string
print("x is {}".format(x))
#try to check the functions of .format(x)

#lesson 5 conditionals
print("Lesson 5 Conditionals")

x = 1
y = input("enter a value")
if y != x:
	print("{} doesn't equal {}".format("x","y"))
elif y == x:
	print(True)
else:
	print("Hawaii")
#lesson 6 lists

print("Lesson 6 Lists")

