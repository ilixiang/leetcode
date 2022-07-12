#!/usr/bin/python3

def isHappy(n):
    s = set()
    while n != 1:
        quotient = n
        n = 0
        while quotient != 0:
            remainder = quotient % 10
            n = n + remainder * remainder
            quotient = quotient // 10
        if n in s:
            return False
        s.add(n)
    return True

print(isHappy(7))
print(isHappy(19))
print(isHappy(2))

