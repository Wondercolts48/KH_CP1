# Kh 2nd texted based adventure game

#Variables

#Bosses = {
	"Buffalo":[80 "HP", 15 "damage"],
	"Alligator":[80 "HP", 15 "damage"],
	"Lion": [100 "HP", 18 "damage"],
	"Camel": [110 "HP", 20 "damage"],
	"Owl":[110 "HP", 20 "damage"],
	"Crane":[90 "HP", 17 "damage"],
	"Moose":[95 "HP", 18 "damage"],
	"Phoenix":[200 "HP", 30 "damage"]
}

#Having to actually make my player
def create_player():
	player = {
		"health": 100,
		"strength":10,
		"defense": 5,
		"temperature_resistance": 0,
		"inventory_visted": [],
		"location_visited": [],
		"weapon": "",
		"crystals_collected": 0,
		"defeated_bosses":[]
	}
	return player
#Defining how my player stats are going to work
def display_stats(player):
    print(f"Health: {player['health']} HP")
    print(f"Strength: {player['strength']}")
    print(f"Defense: {player['defense']}")
    print(f"Temperature Resistance: {player['temperature_resistance']}")
    print(f"Crystals: {player['crystals_collected']}/8")
    print(f"Weapon: {player['weapon']}")

def pick_up(player, item_name):
	if item_name not in player["inventory"]:
		player["inventory"].append(item_name)
        print(f"✓ You have picked up {item_name}!")
    else:
        print(f"You already have {item_name}.")

def use_item(player):
    if not player["inventory"]:
        print("Your inventory is empty!")
        return False
    
    print("\nYour inventory:")
    for i, item in enumerate(player["inventory"], 1):
        print(f"{i}. {item}")
    print(f"{len(player['inventory']) + 1}. Cancel")
    
    try:
        choice = int(input("Choose an item to use: "))
        if choice == len(player["inventory"]) + 1:
            return False
        
        item = player["inventory"][choice - 1]
        
        if "Health Potion" in item:
            player["health"] += 20
            player["inventory"].remove(item)
            print(f"✓ You used a Health Potion! Restored 20 HP. Current HP: {player['health']}")
            return True
        elif "Bandage" in item:
            player["health"] += 8
            player["inventory"].remove(item)
            print(f"✓ You used a Bandage! Restored 8 HP. Current HP: {player['health']}")
            return True
        else:
            print("This item cannot be used in combat.")
            return False
    except (ValueError, IndexError):
        print("Invalid choice!")
        return False

def combat(player,boss_name):
    boss_health = BOSSES[boss_name][0]
    boss_damage = BOSSES[boss_name][1]
    special_attack_count = 0
    
    print(f"\n⚔️  BATTLE START: You vs {boss_name}! ⚔️\n")
    
    while player["health"] > 0 and boss_health > 0:
        print(f"Your HP: {player['health']} | {boss_name}'s HP: {boss_health}")
        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Defend/Block")
        print("3. Use Item")
        if special_attack_count < 2:
            print("4. Special Attack (Remaining: {})".format(2 - special_attack_count))
        
        choice = input("Choose action: ").strip()
        
        defend_mode = False
        
        # Player's turn
        if choice == "1":  # Attack
            damage = player["strength"]
            boss_health -= damage
            print(f"\n You dealt {damage} damage to {boss_name}!")
            
        elif choice == "2":  # Defend
            print("\n You brace yourself and raise your weapon to block!")
            defend_mode = True
            
        elif choice == "3":  # Use Item
            if use_item(player):
                continue  # Skip boss turn if item used successfully
            
        elif choice == "4" and special_attack_count < 2:  # Special Attack
            damage = player["strength"] * 2
            boss_health -= damage
            special_attack_count += 1
            print(f"\n SPECIAL ATTACK! You dealt {damage} damage to {boss_name}!")
            print(f"Special attacks remaining: {2 - special_attack_count}")
        else:
            print("Invalid choice! You hesitate...")
        
        # Check if boss is defeated
        if boss_health <= 0:
            print(f"\n Victory! You have defeated {boss_name}! ")
            player["defeated_bosses"].append(boss_name)
            return True
        
        # Boss's turn
        print(f"\n{boss_name} attacks!")
        damage = boss_damage - player["defense"]
        if defend_mode:
            damage = damage // 2
            print("You blocked! Damage reduced!")
        
        if damage < 0:
            damage = 0
        
        player["health"] -= damage
        print(f" You took {damage} damage! Your HP: {player['health']}")
        
        # Check if player is defeated
        if player["health"] <= 0:
            print("\n YOU HAVE DIED! ")
            print("Respawning at Headquarters...\n")
            player["health"] = 100
            return False
        
        input("\nPress Enter to continue...")
    
    return False

	def check_temperature(player, required_temp, location_name):
    if player["temperature_resistance"] < required_temp:
        print(f"\n WARNING: {location_name} requires {required_temp} temperature resistance!")
        print(f"You only have {player['temperature_resistance']}. You will take 10 damage from the environment.")
        choice = input("Do you want to continue anyway? (yes/no): ").lower()
        
        if choice == "yes":
            player["health"] -= 10
            print(f" You took 10 environmental damage! HP: {player['health']}")
            if player["health"] <= 0:
                print("\n You died from the harsh environment!")
                player["health"] = 100
                return False
            return True
        else:
            return False
    return True

def headquarters(player):
    print(" HEADQUARTERS ")
    print("="*50)
    
    if player["weapon"] == "":
        print("\nWelcome, brave warrior!")
        print("The world is in chaos! 8 corrupted crystals have caused monsters to appear.")
        print("You must collect all crystals and defeat the Phoenix in the Nether to restore peace!\n")
        
        print("Choose your starting weapon:")
        print("1. Sword - Balanced weapon")
        print("2. Axe - High damage")
        print("3. Spear - Quick attacks")
        
        weapon_choice = input("Choose (1-3): ").strip()
        weapons = {"1": "Sword", "2": "Axe", "3": "Spear"}
        player["weapon"] = weapons.get(weapon_choice, "Sword")
        
        print(f"\n✓ You equipped the {player['weapon']}!")
        pick_up(player, "Basic Clothing")
        player["temperature_resistance"] = 10
    
    if "Headquarters" not in player["location_visited"]:
        player["location_visited"].append("Headquarters")
    
    display_stats(player)
    
    print("Where do you want to go?")
    print("1. Plains Village")
    print("2. Swamp Village")
    if player["crystals_collected"] >= 1:
        print("3. Savanna Village")
        print("4. Cherry Blossom Village")
        print("5. Taiga Village")
    if player["crystals_collected"] >= 3:
        print("6. Desert Village")
        print("7. Snowy Village")
    if player["crystals_collected"] >= 8:
        print("8. The Nether (FINAL BOSS)")
    print("9. Check Inventory")
    print("10. View Stats")
    
    choice = input("\nChoose location: ").strip()
    
    if choice == "1":
        plains(player)
    elif choice == "2":
        swamp(player)
    elif choice == "3" and player["crystals_collected"] >= 1:
        savanna(player)
    elif choice == "4" and player["crystals_collected"] >= 1:
        cherry_blossom(player)
    elif choice == "5" and player["crystals_collected"] >= 1:
        taiga(player)
    elif choice == "6" and player["crystals_collected"] >= 3:
        desert(player)
    elif choice == "7" and player["crystals_collected"] >= 3:
        snowy(player)
    elif choice == "8" and player["crystals_collected"] >= 8:
        nether(player)
    elif choice == "9":
        print("\nInventory:", player["inventory"] if player["inventory"] else "Empty")
        input("Press Enter to continue...")
        headquarters(player)
    elif choice == "10":
        display_stats(player)
        input("Press Enter to continue...")
        headquarters(player)
    else:
        print("Invalid choice or location locked!")
        headquarters(player)

def plains(player):
    """Plains Village"""
    print("\n PLAINS VILLAGE ")
    
    if "Plains Village" not in player["location_visited"]:
        player["location_visited"].append("Plains Village")
    
    if "Buffalo" in player["defeated_bosses"]:
        print("You have already defeated the Buffalo here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("\nA massive Buffalo blocks your path!")
    if combat(player, "Buffalo"):
        pick_up(player, "Crystal")
        pick_up(player, "Warm Clothing")
        player["crystals_collected"] += 1
        player["temperature_resistance"] += 10
        player["strength"] += 5
        player["defense"] += 3
        print(f"\n✓ Crystal collected! ({player['crystals_collected']}/8)")
        print("✓ Stats increased!")
    
    input("\nPress Enter to return to Headquarters...")
    headquarters(player)

def swamp (player):
    if "Swamp Village" not in player["location_visited"]:
        player["location_visited"].append("Swamp Village")
    
    if "Alligator" in player["defeated_bosses"]:
        print("You have already defeated the Alligator here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("\nA fierce Alligator emerges from the swamp!")
    if combat(player, "Alligator"):
        pick_up(player, "Crystal")
        pick_up(player, "Swamp Gear")
        pick_up(player, "Bandage")
        player["crystals_collected"] += 1
        player["temperature_resistance"] += 10
        player["strength"] += 5
        player["defense"] += 3
        print(f"\n✓ Crystal collected! ({player['crystals_collected']}/8)")
        print("✓ Stats increased!")
    
    input("\nPress Enter to return to Headquarters...")
    headquarters(player)

def savanna(player):
 if "Lion" in player["defeated_bosses"]:
        print("You have already defeated the Lion here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("\nThe mighty Lion, king of the savanna, roars at you!")
    if combat(player, "Lion"):
        pick_up(player, "Crystal")
        pick_up(player, "Light Clothing")
        player["crystals_collected"] += 1
        player["temperature_resistance"] += 6
        player["strength"] += 5
        player["defense"] += 3
        print(f"\n✓ Crystal collected! ({player['crystals_collected']}/8)")
        print("✓ Stats increased!")
    
    input("\nPress Enter to return to Headquarters...")
    headquarters(player)
