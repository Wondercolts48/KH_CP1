# Kh 2nd texted based adventure game

#Variables

Bosses ={
    "Buffalo":[80,17],
"Alligator":[80,18 ],
"Lion": [100, 23],
"Camel": [110, 25],
"Owl":[120, 24],
"Crane":[102, 21 ],
"Moose":[115,26],
"Phoenix":[200, 46]
}

BOSS_REWARDS = {
    "Buffalo": {
        "temp": 10,
        "crystals": 1,
        "items": ["Warm Clothing"]
    },
    "Alligator": {
        "temp": 10,
        "crystals": 1,
        "items": ["Swamp Gear", "Bandage"]
    },
    "Lion": {
        "temp": 6,
        "crystals": 1,
        "items": ["Light Clothing"]
    },
    "Crane": {
        "temp": 6,
        "crystals": 1,
        "items": ["Silk Garments", "Bandage"]
    },
    "Moose": {
        "temp": 4,
        "crystals": 1,
        "items": ["Fur Clothing", "Bandage"]
    },
    "Camel": {
        "temp": 4,
        "crystals": 1,
        "items": ["Desert Robes", "Health Potion"]
    },
    "Owl": {
        "temp": 6,
        "crystals": 1,
        "items": ["Winter Coat", "Health Potion"]
    },
    "Phoenix": {
        "temp": 0,
        "crystals": 0,
        "items": []
    }
}


def boss_rewards(player,boss_name):
        rewards = BOSS_REWARDS[boss_name]
        player["temperature_resistance"] += rewards["temp"]
        player["crystals_collected"] += rewards["crystals"]
        for item in rewards["items"]:
                pick_up(player, item)
        print("Rewards recieved!")
        print(f"+{rewards['temp']} Temperature Resistance")
        print(f"+{rewards['crystals']} Crystal")
        if rewards["items"]:
                print("Items:", ", ".join(rewards["items"]))

#Having to actually make my player
def create_player():
	player = {
		"health": 80,
		"strength":9,
		"defense": 5,
		"temperature_resistance": 0,
		"inventory": [],
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
        print(f" You have picked up {item_name}!")
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

def combat(player, boss_name):
    boss_health = Bosses[boss_name][0]
    boss_damage = Bosses[boss_name][1]
    special_attack_count = 0
    
    print(f" BATTLE START: You vs {boss_name}!")
    
    while player["health"] > 0 and boss_health > 0:
        print(f"Your HP: {player['health']} | {boss_name}'s HP: {boss_health}")
        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Defend/Block")
        print("3. Use Item")
        if special_attack_count < 2:
            print(f"4. Special Attack (Remaining: {2 - special_attack_count})")
        
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
            print(f"SPECIAL ATTACK! You dealt {damage} damage to {boss_name}!")
            print(f"Special Attack (Remaining: {2 - special_attack_count})")
        else:
            print("Invalid choice! You hesitated...")
        
        # Check if boss is defeated
        if boss_health <= 0:
            print(f" Victory! You have defeated {boss_name}! ")
            player["defeated_bosses"].append(boss_name)
            boss_rewards(player, boss_name)
            player['health'] = 100
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
            print("Respawning at Headquarters...")
            player["health"] = 100
            break
        
        input("Press Enter to continue...")
    
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
                print(" You died from the harsh environment!")
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
        print("Welcome, brave warrior!")
        print("The world is in chaos! 8 corrupted crystals have caused monsters to appear.")
        print("You must collect all crystals and defeat the Phoenix in the Nether to restore peace!")
        
        print("Choose your starting weapon:")
        print("1. Acorn rings - 12 damage, the special attack does 25 damage")
        print("2. Bunny braclet - 14 damage, special attack does 16 ")
        print("3. Serpant fan - 15 damage, special attack does 23")
        print("4. Flower scythe - 13 damage, special attack does 17 ")
        
        weapon_choice = input("Choose (1-4): ").strip()
        weapons = {"1": "Acorn rings", "2": "Bunny braclet", "3": "Serpant fan", "4": "Scythe"}
        player["weapon"] = weapons.get(weapon_choice, "Sword")
        
        print(f"You equipped the {player['weapon']}!")
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
    
    choice = input("Choose location: ").strip()
    
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
        print("Inventory:", player["inventory"] if player["inventory"] else "Empty")
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
    print(" PLAINS VILLAGE ")
    
    if "Plains Village" not in player["location_visited"]:
        player["location_visited"].append("Plains Village")
    
    if "Buffalo" in player["defeated_bosses"]:
        print("You have already defeated the Buffalo here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("\nA massive Buffalo blocks your path!")
    if combat(player, "Buffalo"):
        player["strength"] += 2
        player["defense"] += 3
        print(f" Crystal collected! ({player['crystals_collected']}/8)")
        print("Stats increased!")
    
    input("Press Enter to return to Headquarters...")
    headquarters(player)

def swamp (player):
    if "Swamp Village" not in player["location_visited"]:
        player["location_visited"].append("Swamp Village")
    
    if "Alligator" in player["defeated_bosses"]:
        print("You have already defeated the Alligator here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("A fierce Alligator emerges from the swamp!")
    if combat(player, "Alligator"):
        pick_up(player, "Swamp Gear")
        player["strength"] += 2
        player["defense"] += 3
        print(f"Crystal collected! ({player['crystals_collected']}/8)")
        print("Stats increased!")
    
    input("\nPress Enter to return to Headquarters...")
    headquarters(player)

def savanna(player):
    if "Lion" in player["defeated_bosses"]:
        print("You have already defeated the Lion here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    if combat(player, "Lion"):
        pick_up(player, "Light Clothing")
        player["strength"] += 2
        player["defense"] += 3
        print(f"Crystal collected! ({player['crystals_collected']}/8)")
        print(" Stats increased!")
        
        input("\nPress Enter to return to Headquarters...")
    headquarters(player)

def desert(player):
    """Desert Village"""
    print("DESERT VILLAGE ")
    if not check_temperature(player, 30, "Desert Village"):
        headquarters(player)
        return

    if "Desert Village" not in player["location_visited"]:
        player["location_visited"].append("Desert Village")
    
    if "Camel" in player["defeated_bosses"]:
        print("You have already defeated the Camel here.")
        input("Press Enter to return...")
        headquarters(player)
        return

    if combat(player, "Camel"):
        pick_up(player, "Desert Robes")
        player["strength"] += 2
        player["defense"] += 3
    
    input("Press Enter to return to Headquarters...")
    headquarters(player)

def snowy(player):
    print(" SNOWY VILLAGE")
    if not check_temperature(player, 30, "Snowy Village"):
        headquarters(player)
        return
    
    if "Snowy Village" not in player["location_visited"]:
        player["location_visited"].append("Snowy Village")
    
    if "Owl" in player["defeated_bosses"]:
        print("You have already defeated the Owl here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("A mystical Ice Owl swoops down from the sky!")
    if combat(player, "Owl"):
        pick_up(player, "Crystal")
        pick_up(player, "Winter Coat")
        player["strength"] += 2
        player["defense"] += 3
        print(f" Crystal collected! ({player['crystals_collected']}/8)")
        print(" Stats increased!")
    
    input("Press Enter to return to Headquarters...")
    headquarters(player)

def cherry_blossom(player):
    """Cherry Blossom Village"""
    print(" CHERRY BLOSSOM VILLAGE ")

    if not check_temperature(player, 15, "Cherry Blossom Village"):
        headquarters(player)
        return
    
    if "Cherry Blossom Village" not in player["location_visited"]:
        player["location_visited"].append("Cherry Blossom Village")
    
    if "Crane" in player["defeated_bosses"]:
        print("You have already defeated the Crane here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("An elegant Crane warrior challenges you!")
    if combat(player, "Crane"):
        pick_up(player, "Silk Garments")
        player["strength"] += 3
        player["defense"] += 3
        print(f" Crystal collected! ({player['crystals_collected']}/8)")
        print("Stats increased!")
    
    input("\nPress Enter to return to Headquarters...")
    headquarters(player)

def taiga(player):
    """Taiga Village"""
    print(" TAIGA VILLAGE ")
    
    if not check_temperature(player, 15, "Taiga Village"):
        headquarters(player)
        return
    
    if "Taiga Village" not in player["location_visited"]:
        player["location_visited"].append("Taiga Village")
    
    if "Moose" in player["defeated_bosses"]:
        print("You have already defeated the Moose here.")
        input("Press Enter to return...")
        headquarters(player)
        return
    
    print("A giant Moose crashes through the trees!")
    if combat(player, "Moose"):

        pick_up(player, "Fur Clothing")

        player["strength"] += 2
        player["defense"] += 3
        print(f"Crystal collected! ({player['crystals_collected']}/8)")
        print("Stats increased!")
    
    input("\nPress Enter to return to Headquarters...")
    headquarters(player)

def nether(player):
    """The Nether - Final Boss"""
    print(" THE NETHER ")
    print("The Phoenix, source of all corruption, awaits!")
    
    if "Nether" not in player["location_visited"]:
        player["location_visited"].append("Nether")
    
    if combat(player, "Phoenix"):
        print("" + "="*50)
        print(" CONGRATULATIONS! ")
        print("="*50)
        print("You have defeated the Phoenix and collected all 8 crystals!")
        print("Peace has been restored to the world!")
        print("You are a true BEAST BLASTER!")
        print("="*50 + "\n")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            new_player = create_player()
            start_game(new_player)
        else:
            print("Thanks for playing!")
            return
    else:
        headquarters(player)

def start_game(player):
    """Start the game"""
    print("" + "="*50)
    print("  BEAST BLASTERS: CRYSTALS CLEANUP")
    print("Welcome to Beast Blasters!")
    
    choice = input("\nDo you want to start your adventure? (yes/no): ").lower()
    
    if choice == "yes":
        headquarters(player)
    else:
        print("Maybe another time! Goodbye!")

# Starting the game
if __name__ == "__main__":
    player = create_player()
    start_game(player)
