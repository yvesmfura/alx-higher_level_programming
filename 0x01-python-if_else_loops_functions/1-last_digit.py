#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
lastd = abs(number) % 10

if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd == 0:
    print(f"Last digit of {number} is {lastd} and is 0")
else:
    if number < 0:
         print(f"Last digit of {number} is  -{lastd}
	 and is less than 6 and not 0")
    else:
         print(f"Last digit of {number} is  {lastd}
	 and is less than 6 and not 0")
=======
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
>>>>>>> 784973433d87e1fe18b131f48c2426976b860264
