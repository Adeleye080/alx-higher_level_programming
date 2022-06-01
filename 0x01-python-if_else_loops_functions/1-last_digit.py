#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1

message = f"Last digit of {number:d} is {last_digit:d}"

if last_digit > 5:
    print(message + " and is greater than 5")
elif last_digit == 0:
    print(message + " and is 0")
elif last_digit < 6 != 0:
    print(message + " and is less than 6 and not 0")
