# KH 2nd string methods notes

name = input("What is your name?").strip().title()
#.lower() => makes it all lower case
# .upper() => all upper case
# .capitalize() => capitalize the first letter
# .title() => capitalize the first letter of every word

age = int(input("Bro how old are you?"))
print("Hello {}, it is nice to meet you! I can't believe you are {:3f}!".format(name, age)) 

print(f"Hello {name}, it is nice to meet you! I can't believe you are {age:.1f}!".format(name, age)) 


#age = input("Bro how old are you?")

#print(age.isdigit())

#print("Really? "+ age + " is old")

#sentence = "The quick brown fox jumps over the lazy dog!"

#word = "brown"
#print(sentence.find("fox"))
#start = sentence.find(word)
#length = len(word)

#print(sentence.replace[word, "yellow"])
