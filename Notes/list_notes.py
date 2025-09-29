# KH 2nd List notes
import random

names =["Alex", "Katie" , "Cora"," Andrew", "Jake", "Eric", 5, 3.14, 14, False] #Needs to have a bracket, straight ones

print(names)
print(names[3])
print(names[random.randint(1,len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names +=["Joseph", "Isreal", "Zee"]
names.remove(3.14)
x = names.index(5)
names.insert(3, "Vienna")
names.pop(x)
print(names)



board = [[1,2,3],
         [4,5,6,],
         [7,8,9]]
board[1][1] = "X"

print(board)
# list (changeable, ordered)
# Tuple (not changeable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")

# Set (changeable, unordered)
fruit = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruit)