# Kh 2nd Shopping List Manager

shopping_list = []
while True:
    action = input("What would you like to do to your list? Do you want to view, remove, or add to your list? ")
    if action == "add":
        new_item = input("What would you like to add to your list?")
        shopping_list.append(new_item)
        print(f"Here is your new shopping list {shopping_list}")
    elif action == "remove":
        remove_item = input("What would you like to remove from your list?")
        shopping_list.remove(remove_item)
        print("You removed", remove_item, "from your list, this is your new list now", shopping_list)
    elif action == "view":
        print(shopping_list)
    elif action == "exit":
        print("Goodbye")
        break
    else: 
        print("That's not an option from your list")