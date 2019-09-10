#!/usr/bin/env python3
def print_last_digit(number):
    num = abs(number)
    num = num % 10
    print("{}".format(num), end="")
    return (num)
