#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
neg = -last
if number < 0:
    print(f"Last digit of {number} is {neg} and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is zero")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
