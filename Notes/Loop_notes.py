# Kh 2nd For loops notes
import time

nums = [6,51,61,94,351,946,5489,4,654,684]

for num in nums:
    div = num/2
    if div >100:
        print(f"{div} is half of {num}. And it is still a larger number!")
    else:
        print(nums)

print("We have completed all the numbers!")
time.sleep(3)
for x in range(2,11):
    print(x)
time.sleep(3)

print("Count by twos")
for x in range(2,11,2):
    print(x)
time.sleep(3)

print("Count down")
for x in range(10,0,-1):
    print(x)
    time.sleep(1) #Tells you how long the code should wait until the next thing