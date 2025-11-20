# Kh 2nd sqaured numbers

#Having my list with at least 20 numbers
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230,]

print(len(numbers))
# Getting the variable for when I have to square - use sqr
sqr = []
# Putting my lambda function for when I square 
sqaured = list(map(lambda num: num**2, numbers))
# Then printing out my function
for i, num in enumerate(numbers):
      print(f'original: {num}, squared: {sqaured[i]}')
