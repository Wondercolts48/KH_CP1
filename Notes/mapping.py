# Kh 2nd mapping notes

numbers = [641,45,34,5,43,54,34,5,4,3,453,45]
divided = []

for num in numbers:
    divided.append(num/2)

def divide(number):
        return number/2

divided = list(map(lambda num: num/2, numbers))    # Lambda functions

print(divided)

for i, num in enumerate(numbers):
      print(f'{num} divided by 2 is {divided[i]}')

