#  Kh 2nd *args and *kwargs notes

"""def hello(name = "Tia", age =29):
    return f"hello {name}! You are {age}"

print(hello())
print(hello("Xavier"))
print(hello(name = "Treyson", age = 19))"""


# ARGS
#Positional arugements, *args, Keywords arguments, **kwargs
def hello(*names, **last):
    print(type(names))
    print(last)
    for name in names:
        if name == "Vienna":
            print(f"Helo {name} {last['alast']} {last['vlast']}")
        else:
            print(f"Hello {name} {last['alast']}")

hello("Alexander", "Kathryn", "Andrew", "Vienna", "Tia", " Treyson", "Xavier", "Jake", alast = "LaRose", vlast= "Atkin") 