# KH 2nd format outputs notes

name = "Jake"
age = 21
grade = .75
money = 25

print("hello {}, nice to meet you!. You are {:E}, that is really old! You have a {:%} in this class. You have ${:.2f}, that is a lot of money!".format(name,age,grade, money))

#Different format method
print(f"hello {name}, nice to meet you!.\nYou are {age:E}, that is really old! \nYou have a {grade:%} in this class. \nYou have ${money:.2f}, that is a lot of money!")