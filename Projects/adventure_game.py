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

#THE MAIN GAME
#Start game:
#Display the title screen and introduction
#Sets all the users stats, makes all their lists empty and calls the Headquarters function




# All 9 locations as function. All are functions
def	headquarters():
    print(input("Hello! Welcome to Beast Blasters: Crystals Cleanup! Would you like to play today? "))
    if user == "Yes":
        print("Great!")

#Gives the user a piece of clothing so they can go to other places first
#Can choose between going to the plains or swamp
#Displays which villages they can go to - only to 8, the Nether is last
#Shows how many crystals they have gotten
    print("Right now you have 0 crystals")
#Lets users choose which village they can go to
#Stores the weapon they choose in the variable of weapon
#Adds “headquarters to location_visited
#Tells them that they have to go out and come back to leave the crystals to return peace to the world
headquarters()



