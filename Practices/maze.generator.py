#Kh 2nd maze generator

#Importing the things I need
import random
import turtle

grid_rows = random.randrange(0,1)

grids_columns = random.randrange (0,1)

turtle.goto(0,0)
#making my borders so then I can make the maze
for grid in range(20):
   if grid == 0:        #Making the borders
      turtle.forward(360)
      turtle.penup()
      turtle.right(90)


   if grid == 1:
         turtle.penup()
         turtle.forward(50)
         turtle.pendown()
         turtle.forward(200)

   if grid == 2:
      turtle.forward(60)
      turtle.right(90)


   if grid == 3:
         turtle.forward(80)
         turtle.pendown()
         turtle.forward(220)

   if grid == 4:
      turtle.forward(60)
      turtle.penup()
      turtle.right(90)

   if grid == 5:
         turtle.penup()
         turtle.forward(50)
         turtle.pendown()
         turtle.forward(260)
         turtle.penup()
         turtle.goto(0,-260)
         turtle.right(90)
# Going to make my rows and columns
def grid_rows():
   val = random.randrange(0,1)
   if val == 0:
       turtle.pendown
       turtle.color("black")
       turtle.forward(30)
   elif val == 1:
       turtle.penup




def grids_columns():
   if grids_columns == 0:
      turtle.penup




grid_rows()


grids_columns()

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