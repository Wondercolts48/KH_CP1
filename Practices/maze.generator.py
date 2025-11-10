#Kh 2nd maze generator

#Importing the things I need
import random
import turtle

grid_rows = [
    [],
    [],
    [],
    [],
    [],
    [],
]

grids_columns = [
    [],
    [],
    [],
    [],
    [],
    [],
]

# Setup turtle
turtle.hideturtle()
turtle.speed(0)


# Going to make my rows and columns
def makerows(grid_rows):
   for row in grid_rows:
      for i in range(0, 6):
         row.append(random.randrange(0, 2))


def makecolumns(grids_columns):
   # Fill the columns grid
   for col in grids_columns:
      for i in range(0, 6):
         col.append(random.randrange(0, 2))


# To draw the borders
def draw_border(num_rows, num_cols):
   cell_size = 50  # Size of each cell in pixels
   start_x = -150  # Starting x position
   start_y = 150  # Starting y position

   # Calculate the total width and height of the maze
   width = num_cols * cell_size
   height = num_rows * cell_size

   turtle.penup()
   turtle.goto(start_x, start_y)
   turtle.pendown()
   turtle.pensize(3)  # Make the border thicker
   turtle.color("black")

   # Drawing the border
   for _ in range(2):
      turtle.forward(width)
      turtle.right(90)
      turtle.forward(height)
      turtle.right(90)

   turtle.pensize(1)  # Reset pen size to normal
   turtle.penup()


# drawing the maze 
def draw_maze(grid_rows, grids_columns):
   cell_size = 50  # Size of each cell in pixels
   start_x = -150  # Starting x position
   start_y = 150  # Starting y position

   turtle.speed(0)  # Fastest drawing speed
   turtle.penup()

   # Seeing if it should draw the rows
   for row_index, row in enumerate(grid_rows):
      for col_index, has_wall in enumerate(row):
         if has_wall == 1:  # 1 means there's a wall
            # Calculate position
            x = start_x + (col_index * cell_size)
            y = start_y - (row_index * cell_size)

            # Draw the rows
            turtle.goto(x, y)
            turtle.pendown()
            turtle.goto(x + cell_size, y)
            turtle.penup()

   # Seeing if they should draw the columns
   for col_index, col in enumerate(grids_columns):
      for row_index, has_wall in enumerate(col):
         if has_wall == 1:  # 1 means there's a wall
            # Seeing where to start
            x = start_x + (col_index * cell_size)
            y = start_y - (row_index * cell_size)

            # Draws the columns
            turtle.goto(x, y)
            turtle.pendown()
            turtle.goto(x, y - cell_size)
            turtle.penup()


# Seeing if the maze is actually solvable
def is_solvable(row_grid, col_grid):
   # Check if you can get from the top to the bottom
   
   size = len(row_grid)  # Should be 6 (6x6 grid)
   visited = set()  # Keep track of cells we've already checked
   stack = [(0, 0)]  # Start at top-left corner
   
   while stack:
      row, col = stack.pop()
      
      # Checking if the maze is solvable
      if row == size - 1 and col == size - 1:
         return True  # Maze is solvable!
      
      # Skipping the ones we've already checked
      if (row, col) in visited:
         continue
      visited.add((row, col))
      
      # Checking if it can move down
      if row < size - 1 and row_grid[row][col] == 0:
         stack.append((row + 1, col))
      
      # Checking if it can move right
      if col < size - 1 and col_grid[col][row] == 0:
         stack.append((row, col + 1))
      
      # Try moving UP (check the wall above the current position)
      if row > 0 and row_grid[row - 1][col] == 0:
         stack.append((row - 1, col))
      
      # Try moving LEFT (check the wall to the left)
      if col > 0 and col_grid[col - 1][row] == 0:
         stack.append((row, col - 1))
   
   return False  # Couldn't reach the goal - maze is not solvable


makerows(grid_rows)
makecolumns(grids_columns)

# Check if the maze is solvable
if is_solvable(grid_rows, grids_columns):
   print("This maze is solvable! You can get from start to finish!")
else:
   print("This maze is NOT solvable - you can't reach the end.")

# Draw the border first
draw_border(6, 6)  # 6 rows and 6 columns

# Draw the maze using the grid data
draw_maze(grid_rows, grids_columns)

turtle.done()




makerows(grid_rows)

grids_columns()

turtle.done()