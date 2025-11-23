# Kh 2nd factorial calculator

# Defining factorial calculator/calc function(userinput)
def factorial(n)
user_input = int(input("Enter a number: "))  #userinput
result = 1
#For x in range(user_input-1)
for x in range( x, user_input - 1):
    result = result * 1   # Added what happens when you get the result because my partner forgot
return result

#While True
while True:
#Use-choice is an integer: , (int method)
    if (user_input) == int:
        print("")
        break     #Break

#else: print/ displaying that the user needs to type an integer
    else:
        print("You need to put in an actual integer")
