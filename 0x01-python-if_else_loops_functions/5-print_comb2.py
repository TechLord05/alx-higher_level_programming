#!/usr/bin/python3
for num in range(100):
    end = '\n' if num == 99 else ', '
    print("{:02d}".format(num), end=end)
