#Kh 2nd maze generator

#Importing the things I need
import random
import turtle


line_1 = turtle.Turtle()

line_1.pendown()
line_1.forward(350)






turtle.done()
# Seeing if the maze is actaully solvable
def is_solvable(row_grid, col_grid):

    size = len(row_grid) - 1  #how wide the maze actaully is'
    visited = []   #Seeing where we have been already
    stack = [(0, 0)]  #Places we alrady have been

    while stack:
     x, y = stack.pop

     if x == size - 1 and y == size - 1:
         return True
     
     if (x , y) in visited:
         continue
     visited.add((x,y))

     if x < size - 1 and col_grid [y][x+1] == "":
        stack.append((x + 1, y))

    if y < size - 1 and row_grid [y + 1][x] == 0:
       stack.append((x , y + 1))

    if x > 0 and col_grid[y][x] == 0:
       stack.append((x -1, y))

    if y > 0 and row_grid[y][x] == 0:
       stack.append((x, y -1))

    return False