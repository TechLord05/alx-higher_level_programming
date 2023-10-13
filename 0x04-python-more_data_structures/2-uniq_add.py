#!/usr/bin/python3

def uniq_add(my_list=[]):
    return sum(set(num for num in my_list if isinstance(num, int)))
