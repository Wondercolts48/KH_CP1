# KH 2nd Cesar cypher encoder and decoder
# Make a function to cypher up the message
def encode():
      # Ask what they want to do cypher
    message = input("Hi, please put in your code you want to cypher ") 
       #Make the whole code shift how many spaces the user wants
    move = input("How many spaces do you want to shift? ")
    # Have all my variables in a place where I can see
    letter = ""
    shift = int(shift)

    for letter in message:
        cypher = ord(letter) + shift
        cypher = chr(cypher)
    #then it prints out the code after it's already cyphered

    print(message)