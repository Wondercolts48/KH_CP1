# kh 2nd Making a turtle race

#Importing the libraries I need
import turtle
import random

def speed():
    t1.forward(random.randrange(1, 72))
    t2.forward(random.randrange(1, 72))
    t3.forward(random.randrange(1, 72))
    t4.forward(random.randrange(1, 72))
    t5.forward(random.randrange(1, 72))
    



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


t2.color("Red")
t2.shape("turtle")   #Make sure the variables are a turtle, like the animal
t2.penup()
t2.goto(-480,210)


t3.color("Orange")
t3.shape("turtle")   #Make sure the variables are a turtle, like the animal
t3.penup()
t3.goto(-480,10)


t4.color("Light pink")
t4.shape("turtle")   #Make sure the variables are a turtle, like the animal
t4.penup()
t4.goto(-480,-210)

t5.color("Light blue")
t5.shape("turtle")   #Make sure the variables are a turtle, like the animal
t5.penup()
t5.goto(-480,-410)

#Making my finished line
turtle.penup()
turtle.goto(500,540)
turtle.pensize(14)
turtle.pendown()
turtle.right(90)
turtle.forward(2000)

#Making a While True
while True:
    speed()


turtle.done()