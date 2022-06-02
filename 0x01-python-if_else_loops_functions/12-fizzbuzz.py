#!/usr/bin/python3
def fizzbuzz():
    for nummber in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz', end='')
        elif number % 5 == 0:
            print('Buzz', end='')
        elif number % 3 == 0:
            print('Fizz', end='')
        else:
            print(number, end='')

        print(" ", end='')
