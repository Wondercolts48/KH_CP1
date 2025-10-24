# Kh 2nd Combat program


player = input("Welcome to training! First up, what is your name? ")
print("Welcome", player)

Class = input("Now choose your class of fighter, 1 is a fighter, 2 is a wizard, 3 is a spy. ")
print("Great, here are your stats!")

if Class == 1:
   
   health = str(20)
   print(str(health))
   defense = 40
   print(str(defense))
   damage = 15
   print(str(damage))

elif Class == 2:
   health = 15
   defense = 25
   damage = 30

elif Class == 3:
    health = 15
    defense = 10
    damage = 10
