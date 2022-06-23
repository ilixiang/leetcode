#!/usr/bin/python3

def myPow(x, n):
    if n == 0:
        return 1.0
    if n == 1:
        return x

    if n < 0:
        return 1.0 / myPow(x, -1 * n)

    num = myPow(x, n // 2)
    return num * num * (x if n % 2 == 1 else 1.0)

print(myPow(2.1, 3))

