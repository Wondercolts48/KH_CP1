# Kh 2nd User sign in

user = input("Please put in your username. ")
password = input("Now put in your password. ")

user_again = input("Put it your username again. ")
password_again = input("Put in your password again. ")

if user == user_again:
    if password == password_again:
        print("Welcome, you can now enter the program")
    else:
        print("Your password is incorrect. ")
else:
    print("Your incorrect, please retype your username or password. ")