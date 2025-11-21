# Kh 2nd a random starter

import turtle

def draw_branch(length):
    if length > 5:
        turtle.forward(length)
        draw_branch(length / 3)
        turtle.back(length)
        turtle.right(60)



turtle.speed(10)
turtle.color("light blue")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()


for i in range:
    draw_branch(100)
    turtle.right(60)

turtle.hideturtle()


turtle.done()