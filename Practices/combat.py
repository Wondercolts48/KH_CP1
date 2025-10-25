# Kh 2nd Combat program

import random   #See's if the user or the Monster will go first
player = input("Welcome to training! First up, what is your name? ")
print("Welcome", player)

Class = input("Now choose your class of fighter, 1 is a fighter, 2 is a wizard, 3 is a spy. ")
print("Great, here are your stats!")

if Class == str(1):
   
   health = (20)
   print(health)
   defense = 40
   print(defense)
   damage = 15
   print(damage)

elif Class == str(2):
   health = 15
   print(health)
   defense = 25
   print(defense)
   damage = 30
   print(damage)

elif Class == str(3):
    health = 15
    print(health)
    defense = 10
    print(defense)
    damage = 10
    print(damage)

turn = random.choice(["user", "monster"])

if turn == "user":
   print("You will go first")
else:
   print("The monster goes first!")

combat_method = input("Choose which combat ")