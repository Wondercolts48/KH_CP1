# Kh 2nd texted based adventure game

#Variables
#Defining how my player stats are going to work
def player_stats():
    player_health = 100  		# How much HP the user has
    player_strength = 10 #changes when the user choose a weapon. Does normal damage
    Player_defense = 5    	 # Reduced impact from the monster  
    Temperature_resistance = 0 	# Protects the user from environment damage

player_stats()

#Lists - where they can put their stuff and see where they have already gone
inventory = []   	#Stores what they have picked up
location_visted = []   	 # Tracks which villages the user has been to
available_weapons = []   	 # Shows which weapon they chose
Crystals_collected = 0  	 # Counts how many crystals the user has
Defeated_bosses = []   	 # Shows how many bosses they have defeated

# Dictionaries
#Has the weapon name
#How much damage it does
#And how much the special attack does too
weapons = {
    "rings": {
    "Name":"Acorn rings",
    "Damage": 10,
    "Special_attack" : 20
    },
    "Bunny braclet":{
        "Damage": 14,
        "Special attack": 17,
    },
    "serpent fan":{
        "Damage": 15,
        "Special attack": 18,
    },

    "Flower Scythe":{
        "Damage": 13,
        "Special attack": 19
    }
}

Bosses = {
    "Buffalo":{
        "Health": 100,
        "Damage": 18

    },
    "lion":{
        "HP": 100,
        "Damage": 15
    },
    "Camel":{
        "HP": 100,
        "Damage": 20
    },
    "Owl":{
        "HP": 110,
        "Damage": 19
    },
    "Crane":{
        "HP": 108,
        "Damage": 15
    },
    "Alligator":{
        "HP": 110,
        "Damage": 17
    },
    "Moose":{
        "HP"": 

    },
    "The Phoenix":{

    }

}


for x in weapons.keys():
    print(x)
    for y in weapons[x].keys():
        print(f"{y} {weapons[x][y]}")
print("")