# Kh 2nd Password strength checker

# have variables as total and special characters

total = 0


#  Ask the user to type in their password
password =("Please type in your new password ")
print(password)

# Remind them that the password has to be 8 characters long, one uppercase letter, one lowercase, one number, and has to have on special character.

# Check if the user put one uppercase, one lowercase using .upper and .lower
# If they have one uppercase you get one points. One lowercase gets you one point
#  has atleast 8 characters(.len), one number(.isdigit) and a special character (.alnum).
# Has more than 8 character they get one point. They have one number they get a point. If they have a special character they get a point.

# See how many point they got from 1-5 on how strong their password is by using the requirments listed.
# 1-2 is weak
# 3 points is okay but not well
#4 points is strong
#5 points is very strong