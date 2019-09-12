#!/usr/bin/python3
import calculator_1
a = 10
b = 5
suma = calculator_1.add
sub = calculator_1.sub
mul = calculator_1.mul
div = calculator_1.div
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, suma(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
