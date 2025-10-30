# kh 2nd Making a turtle race

#Importing the libraries I need
import turtle
import random

#Putting the speed of the turtles
def speed():
    t1.forward(random.randrange(1, 100))
    t2.forward(random.randrange(1, 100))
    t3.forward(random.randrange(1, 100))
    t4.forward(random.randrange(1, 100))
    t5.forward(random.randrange(1, 100))
    
Game = True


#Have all my turtle's be a turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

#Change my turtle colors
t1.color("Light green")
t1.shape("turtle")     #Make sure the variables are a turtle, like the animal
t1.penup()
t1.goto(-480,410)
t1.pensize(5)
t1.pendown()


t2.color("Red")
t2.shape("turtle")   #Make sure the variables are a turtle, like the animal
t2.penup()
t2.goto(-480,210)
t2.pensize(5)
t2.pendown()


t3.color("Orange")
t3.shape("turtle")   #Make sure the variables are a turtle, like the animal
t3.penup()
t3.goto(-480,10)
t3.pensize(5)
t3.pendown()


t4.color("Light pink")
t4.shape("turtle")   #Make sure the variables are a turtle, like the animal
t4.penup()
t4.goto(-480,-210)
t4.pensize(5)
t4.pendown()

t5.color("Light blue")
t5.shape("turtle")   #Make sure the variables are a turtle, like the animal
t5.penup()
t5.goto(-480,-410)
t5.pensize(5)
t5.pendown()

#Making my finished line
turtle.penup()
turtle.goto(500,540)
turtle.pensize(14)
turtle.pendown()
turtle.right(90)
turtle.forward(2000)

#Making a While True
while Game == True:
    speed()
    #Makes the x work and to solve numbers
    t1pos = (round(t1.xcor(), 5))
    t2pos = (round(t2.xcor(), 5))
    t3pos = (round(t3.xcor(), 5))
    t4pos = (round(t4.xcor(), 5))
    t5pos = (round(t5.xcor(), 5))
    
    # Seeing which one will win first so it gives us the result
    if t1pos > 540:
        print("Turtle one won!")
        Game = False
    if t2pos > 540:
        print("Turtle two won!")
        Game = False
    if t3pos > 540:
        print("Turtle three won!")
        Game = False
    if t4pos > 540:
        print("Turtle four won!")
        Game = False
    if t5pos > 540:
        print("Turtle five won!")
        Game = False

turtle.done()