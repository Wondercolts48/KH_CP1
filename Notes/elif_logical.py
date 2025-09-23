# Kh 2nd Elif and Logical operators notes

homework = True
chores = True
room = False

if homework and chores and room:
    print("You can go to your friends house")
elif not chores or not room:
    print("Do your chores and clean your room!")
else:
    print("Go do your homework.")
    
username = input("Enter your username: ")
password = input ("Enter your password: ")

if username == "MsLarose":
        if password == "1234":
            print("Welcome Ms. Larose")
        else:
            print("incorrect password")
elif username == "Tia" and password == "Password":
        print("Welcome Tia.")
elif username == "Andrew" and password =="orange":
        pass
        print("Welcome Andrew")
else:
        print("that is not a vaild sign in.")