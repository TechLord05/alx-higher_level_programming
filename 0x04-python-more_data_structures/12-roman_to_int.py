#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    total = 0
    prev_value = 0

    for index, char in enumerate(roman_string):
        current_value = roman_values.get(char, 0)

        if current_value > prev_value and index > 0:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        prev_value = current_value

    return total
