# Kh 2nd Multiplication table

multi = ()

for multi in range (1,13):
    for x in range (1,13):
        print(f"{multi * x:4}" , end="")
    print()