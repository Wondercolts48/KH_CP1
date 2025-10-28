# Kh 2nd Combat program

import time
import random

player = input("Welcome to training! First up, what is your name? ")
print("Welcome", player)

Class = input("Now choose your class of fighter, 1 is a fighter, 2 is a wizard, 3 is a spy. ")
print("Great, here are your stats!")

mon_hp = 45
mon_att = 5
mon_def = 13

if Class == str(1):
   
   health = (20)
   print("Your health is", health)
   defense = 40
   print("Your defense is", defense)
   damage = 12
   print("You do", damage,"damage")
   turn = random.choice(["user", "monster"])

elif Class == str(2):
   health = 15
   print("Your health is", health)
   defense = 25
   print("Your defense is", defense)
   damage = 30
   print("you do", damage, "damage")
   turn = random.choice(["user", "monster"])

elif Class == str(3):
    health = 15
    print("Your health is", health)
    defense = 10
    print("Your defense is", defense)
    damage = 10
    print("You do", damage,"damage")
    turn = random.choice(["user", "monster"])
   
def move():
   print("")
   if turn == "user":
            print("You go first!")
            print("Choose an action: ")
            print("1. Attack")
            print("2. defense")
            print("3. Heal")
            playerinput = input("")

   if playerinput == str(1):
               mon_hp2 = mon_hp - damage
               print("You hurt the monster, the monster now has", mon_hp2,"health left" ) 
               time.sleep(1)

   elif playerinput == str(3):
               heal = health + 2
               print("you healed yourself", heal)

   elif turn == "monster":
               print("The monster goes first")
   new_health = health - mon_att
   print("You took", mon_att,"damage, now you have", new_health,"health left")
   time.sleep(1)\

move()