# KH 2nd calculator practice

one_num = int(input("enter your first number" " "))
two_num = float(input("Enter your second number" " "))

add = one_num + two_num
sub = one_num - two_num
division = one_num / two_num
exp = one_num ** two_num
multi = one_num * two_num
modulo = one_num % two_num
int_division = one_num // two_num

print(f"{one_num} + {two_num} = {add:.2f}")
print(f"{one_num} - {two_num} = {sub:.2f}")
print(f"{one_num} / {two_num} = {division:.2f}")
print(f"{one_num} ** {two_num} = {exp:.2f}")
print(f"{one_num} * {two_num} = {multi:.2f}")
print(f"{one_num} % {two_num} = {modulo:.2f}")
print(f"{one_num} // {two_num} = {int_division:.2f}")