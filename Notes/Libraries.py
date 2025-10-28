# Kh 2nd Libraries and built-in function notes
import random
import turtle

turtle.shape("turtle")
turtle.color("Yellow")
turtle.pensize(45)
turtle.fillcolor("pink")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)

turtle.end_fill()


turtle.penup()
turtle.goto(-150,100)
turtle.pendown()
turtle.color("Yellow")
turtle.pensize(45)
turtle.fillcolor("pink")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
 
turtle.end_fill()

turtle.done()
