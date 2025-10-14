# Kh 2nd Password strength checker

# have variables as total and special characters
upper = False
lower = False
number = False
special_characters = False

total = 0
special_character = ['!','@','#','$', '%', '^', '&', '*','(',')']
#  Ask the user to type in their password
password =input("Please type in your new password ")


# Check if the user put one uppercase (using .upper), if they do they get one uppercase they get one point
for char in password:
    if char.isupper():
        upper = True

    elif char.islower():
          lower = True    # If they got one lowercase (using.lower), they get one pointelse:

    elif char.isdigit():      # one number(.isdigit), then they get a point
           number = True
    
    elif char in special_character:      # A special character, they get one point
           special_character =True

    elif len(password) >= 8: #has atleast 8 characters(.len), they get one point
             total +=1        
    else:
     pass   
if upper == True:
    total += 1

if lower == True:
    total += 1

if number == True:
    total += 1

if special_character == True:
    total += 1
    # See how many point they got from 1-5 on how strong their password is by using the requirments listed.

    #5 points is very strong
    if total == 5:
        print("5 points is the strongest password you can get.")

    #4 points is strong
elif total == 4:
     print("4 points is strong, but not the strongest")

    # 3 points is okay but not well
elif total == 3:
        print("3 is okay, but not very good.")

    #1-2 is weak
elif total == 1 or 2:
        print("1-2 is pretty weak")  
        #Tell them how many points they got by how strong it is
        print("you got", total,"points out of 5")
    # Tell them what they missed so they can make it better
