#!/usr/bin/python3

def grayCode(n):
    s = [None] * (2 ** n)
    s[0] = 0
    s[1] = 1
    for i in range(1, n):
        existedLength = 2 ** i
        j =  (2 ** i) - 1
        while j >= 0:
            s[existedLength * 2 - j - 1] = s[j] | (1 << i)
            j = j - 1
    return s

print(grayCode(1))
print(grayCode(2))
print(grayCode(3))

