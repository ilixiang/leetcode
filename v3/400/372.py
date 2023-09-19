#!/usr/bin/python3

def superPow(a, b):
    def exp(x, y):
        if y == 0:
            return 1
        if y & 1 == 0:
            return exp((x * x) % 1337, y >> 1)
        return (exp((x * x) % 1337, y >> 1) * x) % 1337
    a %= 1337
    rev = 1
    cur = a
    i = len(b) - 1
    while i >= 0:
        rev = (rev * exp(cur, b[i])) % 1337
        cur = exp(cur, 10)
        i -= 1
    return rev

