#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dict_sorted = sorted(a_dictionary.keys())

    for key in dict_sorted:
        print("{}: {}".format(key, a_dictionary[key]))
