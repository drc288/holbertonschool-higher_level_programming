#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
fst = "Last digit of "
end = " and is less than 6 and not 0"
end2 = " and is greater than 5"
if number < 0:
    ld = (number * -1) % 10
    ld = ld * -1
    print(fst + "{:d} is {:d}".format(number, ld) + end)
else:
    ld = number % 10
    if ld > 5:
        print(fst + "{:d} is {:d}".format(number, ld) + end2)
    elif ld < 6 and ld != 0:
        print(fst + "{:d} is {:d}".format(number, ld) + end)
    else:
        print(fst + "{:d} is 0 and is 0".format(number))
