#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    c = add(a, b)

    print('{:d} + {:d} = {:d}'.format(a, b, c))

    a = 10
    b = 5
    c = sub(a, b)

    print('{:d} - {:d} = {:d}'.format(a, b, c))

    a = 10
    b = 5
    c = mul(a, b)

    print('{:d} * {:d} = {:d}'.format(a, b, c))

    a = 10
    b = 5
    c = div(a, b)

    print('{:d} / {:d} = {:d}'.format(a, b, c))
