# KH 2nd idiot proof practice

full_name = input("Give your me full name." " ").title().strip()
phone = input("please give me your phone number using dashes please." " ")
gpa = float(input("Now give me your GPA." " "))

print(phone.replace("-"," "))

print(round(gpa,1))

print(f"Welcome" " ", full_name,", is your phone number?", phone.replace("-"," "),",this is also your GPA", (round(gpa,1)))