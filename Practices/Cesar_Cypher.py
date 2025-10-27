# KH 2nd Cesar cypher encoder and decoder

# Make a function to cypher up the message
      def encode():
      # Ask what they want to do cypher
message = input("Hi, please put in your code you want to cypher ")
       #Make the whole code shift how many spaces the user wants
    move = input("How many spaces do you want to shift? ")
    # Have all my variables in a place where I can see
    letter = ""
    move = int(move)

    for letter in message:
        if letter.isalpha():    #Checks if the message are letters
        base = ord("A") if letter.isupper() else ord("a")  #Converts to a number at first, then it converts it back to a letter
        shift = (ord(char) - base + shift) % 26 + base
        result += message(shifted)
    else:
        result += message

 return result
    #then it prints out the code after it's already cyphered

encode()

def decode():        #Decodes the message back to the orignal
     for letter in message:
        if letter.isalpha():    #Checks if the message are letters
        base = ord("A") if letter.isupper() else ord("a")  #Converts to a number at first, then it converts it back to a letter
        shift = (ord(char) - base - shift) % 26 + base
        result += message(shifted)
        else:
        result += message

decode()
