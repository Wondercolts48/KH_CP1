# KH 2nd Function notes
#All imports
# Set global variables
num = 0
player_hp = 100
monster_hp = 100

# Write your functions
def add(x, y):
    return x + y

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]
    return initials

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg



#Writethe rest of the code
while num < add(5, 5):
    print("Duck")
    num += 1
print("Goose")
print(f"Result is: {add(-45345436, 5434634)}")
total = add(56456536, 65356354)
print((add(add(3.14, .85),10)))
add(42,7)


print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are: {initials("Xavier LaRose")}")


monster_hp, player_hp =attack(15, "Monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

monster_hp, player_hp =attack(15, "Player")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

print(f"A = {ord("a")}")
print(f"100 = {chr(100)}")