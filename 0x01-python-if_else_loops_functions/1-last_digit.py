#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastd = abs(number) % 10

if number < 0:
    print(f"Last digit of {number} is -{lastd}")
elif number > 0:
    print(f"Last digit of {number} is {lastd} and is positive")
else:
    print(f"Last digit of {number} is {lastd} and is 0")
