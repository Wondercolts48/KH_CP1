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
crystals_collected = 0  	 # Counts how many crystals the user has
Defeated_bosses = []   	 # Shows how many bosses they have defeated

#THE MAIN GAME
#Start game:
#Display the title screen and introduction
#Sets all the users stats, makes all their lists empty and calls the Headquarters function

# All 9 locations as function. All are functions
def	headquarters():
    print(input("Hello! Welcome to Beast Blasters: Crystals Cleanup!"))
    if user == "yes":
        print(input("Great! Welcome new player. What is your name? "))
#Gives the user a piece of clothing so they can go to other places first
#Can choose between going to the plains or swamp
#Displays which villages they can go to - only to 8, the Nether is last
#Shows how many crystals they have gotten
#Lets users choose which village they can go to
#Stores the weapon they choose in the variable of weapon
#Adds “headquarters to location_visited
#Tells them that they have to go out and come back to leave the crystals to return peace to the world
headquarters()

	#Plains():
def plains():
    print("Sup")
#Can go here first 
#Checks the defeated_bosses list to see if the user already defeated it.
#If the Buffalo is already defeated:
#		Tells the user that they already beat them
#		Asks them to go somewhere else
#If the Buffalo hasn’t been defeated yet:
#	Starts to fight the boss
#	Calls the combat function
#After they won:
#	Drops a crystal and clothes, and adds both to the inventory list
#	Increased crystals_collected by 1
#	Increases temperature_resistance by 10
#	Increases player_strength by 5
#	Increases player_defense by 3
#	Adds “Buffalo” to the defeated_bosses list
#Adds “plains village” to the location_vistied list
#Call that location’s function
plains()
	

#	Savanna():
def savanna():
    print("You are great")
#Can’t come in if the users temperature resistance isn’t 25 or higher
#IF temperature_resistance is less than 25:
#	Warns the user that they will take 10 damage from the heat
#	Ask if they want to continue or to go back
#IF the user wants to continue anyways:
#	It subtracts 10 from the player_health
#BUT if the user has more than 25 they can continue
#Checks if the defeated_bosses list to see if the Lion is already defeated
#IF the Lion is defeated:
#	Tell the player and ask where they want to go next
#IF the lion isn’t defeated:
#	Start the combat function
#After winning:
	#Drops crystals and clothing, adds them to the inventory.
#Increased crystals_collected by 1
#	Increases temperature_resistance by 6
# 	Increases player_strength by 5
# 	Increases player_defense by 3
# Asks the player where they want to go to next
savanna()




# 	Desert():
def desert():
    print("Sup")
# Can only come in once the user has 30 or higher temperature resistance
# IF temperature_resistance is less than 30:
# 	Warns the user that they will take 10 damage from the heat
# 	Ask if they want to continue or to go back
# IF the user wants to continue:
# 	It subtracts 10 from the player_health
# BUT if the user has more than 30 they can continue on
# Checks if the defeated_bosses list to see if the Camel is already defeated
# IF the Camel is defeated:
# 	Tell the player and ask where they want to go next
# IF the camel isn’t defeated:
# 	Starts the combat function
# After winning:
# 	Drops crystals and clothing, adds them to the inventory.
# Increased crystals_collected by 1
# 	Increases temperature_resistance by 4
# Drops a potions- restores 20 health
# 	Increases player_strength by 5
# 	Increases player_defense by 3
# Adds “Camel” to the defeated_bosses list
# Adds “Desert village” to the location_vistied list
# Asks the player where they want to go to next
desert()



# 	Snowy():
def snowy():
    print("Sup")
# Can only come in once the user has 30 or higher temperature resistance
# IF temperature_resistance is less than 30:
# 	Warns the user that they will take 10 damage from the heat
# 	Ask if they want to continue or to go back
# IF the user wants to continue:
# 	It subtracts 10 from the player_health
# Checks if the defeated_bosses list to see if the Camel is already defeated
# IF the Owl is defeated:
# 	Tell the player and ask where they want to go next
# IF the camel isn’t defeated:
# 	Starts the combat function
# After winning:
# 	Drops crystals and clothing, adds them to the inventory.
# Increased crystals_collected by 1
# 	Increases temperature_resistance by 6
# 	Increases player_strength by 5
# 	Increases player_defense by 3
# Adds “Owl” to the defeated_bosses list
# Adds “snowy village” to the location_vistied list
# Asks the player where they want to go to next
# Drops a potions -restores 20 health
snowy()

# 	Cherry blossom():
def cherry_blossom():
    print("Sup")
# Can only come in once the user has 15 or higher temperature resistance
# IF temperature_resistance is less than 15:
# 	Warns the user that they will take 10 damage from the heat
# 	Ask if they want to continue or to go back
# IF the user wants to continue:
# 	It subtracts 10 from the player_health
# Checks if the defeated_bosses list to see if the Crane is already defeated
# IF the Crane is defeated:
# 	Tell the player and ask where they want to go next
# IF the crane isn’t defeated:
# 	Starts the  combat function
# After winning:
# 	Drops crystals and clothing, adds them to the inventory.
# Increased crystals_collected by 1
# 	Increases temperature_resistance by 6
# Drops a bandage - restores 8 health
# 	Increases player_strength by 5
# 	Increases player_defense by 3
# Adds “Crane” to the defeated_bosses list
# Adds “Cherry Blossom village” to the location_vistied list
# Asks the player where they want to go to next
cherry_blossom()


# 	Swamp():
def swamp():
    print("Sup")
# Can go here first too
# Checks the defeated_bosses list to see if the user already defeated it.
# If the Alligator is already defeated:
# 		Tells the user that they already beat them
# 		Asks them to go somewhere else
# If the Alligator hasn’t been defeated yet:
# 	Starts to fight the boss
# 	Calls the combat function
# After they won:
# 	Drops a crystal and clothes, and adds both to the inventory list
# 	Increased crystals_collected by 1
# 	Increases temperature_resistance by 10
# 	Drops a bandage - restores 8 health
# 	Increases player_strength by 5
# 	Increases player_defense by 3
# 	Adds “Alligator” to the defeated_bosses list
# Adds “swamp village” to the location_vistied list
# Call that location’s function
swamp()
	
# 	Taiga():
def taiga():
    print("Sup")
# 15 tmp_res
# IF temperature_resistance is less than 15:
# 	Warns the user that they will take 10 damage from the heat
# 	Ask if they want to continue or to go back
# IF the user wants to continue:
# 	It subtracts 10 from the player_health
# Checks if the defeated_bosses list to see if the Camel is already defeated
# IF the Camel is defeated:
# 	Tell the player and ask where they want to go next
# IF the camel isn’t defeated:
# 	Starts the  combat function
# After winning:
# 	Drops crystals and clothing, adds them to the inventory.
# Increased crystals_collected by 1
# 	Increases temperature_resistance by 4
# Drops a bandage - restores 8 health
# 	Increases player_strength by 5
# 	Increases player_defense by 3
# Adds “Moose” to the defeated_bosses list
# Adds “taiga village” to the location_vistied list
# Asks the player where they want to go to next
taiga()


# 	The nether():
def nether():
    print("Sup")

# 	Starts the  combat function
# After winning:
# 	Drops crystals and clothing, adds them to the inventory.
# Increased crystals_collected by 1
nether()


# #Combat function():
def combat():
    print(player_stats)
# Takes in the boss’s name, health, and their damage
# Display’s player health and boss health
# Set special_attack_count to 0

# Start of LOOP: Keeps repeating while the user health and the bosses health are greater than 0

# # Users turn
# Display “What do you want to do?”
# Show user their action options:
# attack
# 2.Defen/block
# 3.Use Item
# 4.Special Attack (Only is their special_attack_count is less than 2)

# User chooses an action

# IF player choose Attack:
# Calculate damage = weapon damage +player_strength
# Subtract the damage from the bosses health
# Display “You have dealt [damage] damage!”
# Display the bosses remaining health

# IF player chooses Defend/Block:
#             Display "You brace yourself and raise your weapon to block!"
#             Users takes half damage this turn (or reduced damage)
        
#         IF the user chooses Use Item:
#             Display items in inventory
#             User selects health potion or bandage

#             IF the user chooses the health potion:
#                 Add 20 to Users_health
#                 Remove potion from inventory
#                 Display "You used a health potion! Restored 20 HP"

#             IF the user chooses the bandage:
#                 Add 8 to Users_health
#                 Remove bandage from inventory
#                 Display "You used a bandage! Restored 8 HP"
        
#         IF User chooses Special Attack AND their special_attack_count is less than 2:
#             Check which weapon player has
#             Use that weapon's special ability (higher damage)
#             Increase special_attack_count by 1
#             Display "Special attacks remaining: [2 minus special_attack_count]"

# # Checks if the boss is defeated
# IF boss health if it’s 0 or less:
# Display “You have defeated [boss name]”
# BREAK out of the combat loop
# RETURN to village function

# # The bosses turn to attack
# Display “[boss name] attacks!”
# Calculate damage = boss damage - user_defense
# IF user choose defend:
# 	Reduced damage by half
# Subtract damage from user_health
# display”You have token [damage] damage!”
# Display the user’s remaining health

# # LOSING CONDITIONS
#  IF user health is < 0:
# Display “YOU HAVE DIED
# Player respawns at Headquarters with full health and can try again
# Sets the users health to to full health
# Breaks out of the combat loop

# After combat ends:
# 	It resets the special_attack_count to 0 for the next battle.

# #PICK UP FUNCTION
# item_up(item_name):
# Check if item is already in their inventory list
# IF it’s not in their inventory yet
# 	Add the item to their inventory list
# Display “You have picked up [item_name]”
# IF it’s already in their inventory
# 	Display “You already have this item.”


# #Item function():
def item():
    print("Sup")
# Displays all items in their inventory list
# The users chooses wich item they want to choose
# IF they choose the health potion:
# 	Adds 20 health to the user_Health
# 	Removes the potion from their inventory
# Displays “Restored 20 HP”
# If they choose a bandage:
# 	Adds only 8 health
# 	Removes the bandage
# 	Displays “Restored 8 HP”
item()

# #THE MAIN GAME
# Start game:
# Display the title screen and introduction
# Sets all the users stats, makes all their lists empty and calls the Headquarters function

# The Loop:
# While user_health is greater than 0:
# User choose a location and is at the location
# Calls the locations function and calls the combat function
# The user can either go to another location or back to headquarters

# Checks if the crystals_collected = 8:
# IF it’s a yes, then it unlocks the Nether
# Display “You can now enter the Nether! Good luck defeating this boss!”

# Continue loop until the user beat the Phoenix or quits

# # WINNING CONDITIONS
# Once the user defeats all the bosses
# The user has all 8 crystals
# The user also to defeat the Phoenix in the Nether to win
# Display victory message
# Game end
# Ask if the user wants to play again
