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
# Getting the user to start ordering
total = 0
def order(order_list):
While True:
choice = input("What would you like for breakfast today? ")
if choice in menu:
    order_list.append(choice)
    total += menu[choice]
    print(f"{choice.title()} was added
else:
    print("That wasn't a choice on the menu, please choose something from the menu.")
#Telling them their receipt and what they owe
