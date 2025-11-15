# Kh 2nd order up

#Putting my dictionarie menu up
menu = {
    "Breakfast": {    #Getting my breakfast order up
        "The grizz": 15.99,
        "Bruce's meat lover's omelette": 13.99,
        "Mini Volcano": 10.99,
        "Happy cub cakes": 4.99
    },
    "Sides":{   #having all my sides
        "Corn bread muffin": 1.69,
        "French fries": 4.99,
        "Sweet potato fries": 5.79, 
        "Fresh fruit": 6.99
    },
    "Drinks": {   # Getting all my drinks
        "Hot chocolate": 3.49,
        "Chocolate milkshake": 5.99,
        "Coffee": 3.99,
        "Iced tea": 3.49


    }

    }

# Making my menu look nice and presentable so it actually looks like a menu
for x in menu.keys():
    print(x)
    for y in menu[x].keys():
        print(f"{y} price {menu[x][y]}")
print("")
order_list = []
total = 0

# Getting the user to start ordering
while True:
    choice = input("What would you like to order? (or type 'done' to finish): ")
    if choice.lower() == 'done':
        break

found = False
for category in menu:
    if choice in menu[category]:
        order_list.append(choice)
    total += menu[category][choice]
    print(f"{choice.title()} was added for ${menu[category][choice]:.2f}")
    found = True
    break

if not found:
    print("That wasn't on the menu. Please choose something from the menu.")

# Telling them their receipt and what they owe
print("\n" + "="*40)
print("YOUR ORDER:")
for item in order_list:
    print(f"  - {item}")
    print("="*40)
    print(f"Total: ${total:.2f}")
    print("Thank you for your order!")
    print("That wasn't a choice on the menu, please choose something from the menu.")
