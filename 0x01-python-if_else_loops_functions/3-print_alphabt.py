#!/usr/bin/python3

for alpha in range(97, 123):
    if chr(alpha) != 'e' and chr(alpha) != 'q':
        print('{}'.format(chr(alpha)), end='')
