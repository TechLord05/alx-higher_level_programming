#!/usr/bin/python3
def print_last_digit(number):
    r = abs(number) % 10
    print("{}".format(r), end='')
