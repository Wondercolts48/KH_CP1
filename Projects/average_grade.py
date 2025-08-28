#2nd KH average grade project

grade1=float(input("What is your grade in math? "))
grade2= float(input("What is your grade for science? "))
grade3=float(input("What is your grade for english? "))
grade4=float(input("What is your grade for programming? "))
grade5=float(input("What is your grade for history? "))
grade6=float(input("What is your grade for drawing? "))
grade7=float(input("What is your grade for advisory? "))

grade = grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7
grade = grade/7

print(round(grade,2))