# KH 2nd Dictionaries notes

avatar = {
    "earth" : {
        "Toph" : "My name is Toph, cuz it sounds like TOUGH and thats just what I am."
},
        "water" : {
            "katara" : "It's not like I am preachy crybaby who can't help but make speaches about hope all the time.",
            "Sokka" : "I used to be boomerang guy."
},
"fire" : {
    "Suko" : "It jus tkeeps blowing up in my face. Like everything always does!",
} 
    
        }

print(avatar["earth"["Toph"]])


person = {
    # key: value,
    "name": "Katie",
    "age": 37,
    "job": "Coordinator",
    "siblings" : ["Alex", "Andrew", "Vienna", "Tia," "Treyson", "Xavier", "Jake"]
}

print(person["name"])
print(person.keys())

for key in person.keys():
    if key == "Siblings":
        for sib in person[key]:
            print(f"{person["name"]} has a siblings named {sib}")
    else:
        print(f"{key} is {person[key]}")


print(person.values())

person["age"] += 1
print(person["age"])

person["birthday"] = "June 8"
print(person.items())

person["birthday"] = "October 28"
person.items()