# Kh 2nd factorial calculator

# Defining factorial calculator/calc function(userinput)
def factorial(n)
result = 1
#For x in range(user_input-1)
for x in range( n, user_input - 1):   # Had to make changes about the user input
    result = result * x   # Added what happens when you get the result because my partner forgot
return result

factorial()
#While True
while True:
    user_input = int(input("Enter a number: "))  #userinput
    if user_input.isdigit():    # Had to add that we have to find out it's an integer
        user_input = int(user_input)
        answer = factorial(user_input)  
         print(f'original: {user_input}, factorial: {answer}')
#Use-choice is an integer: , (int method)
        print("")
        break     #Breaks out of the loop

#else: print/ displaying that the user needs to type an integer
    else:
        print("You need to put in an actual integer")

