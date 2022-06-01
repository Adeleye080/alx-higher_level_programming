#!/usr/bin/python3
for number in range(00, 100):
    print("{:02d}".format(number), end=', ' if number != 99 else '\n')
