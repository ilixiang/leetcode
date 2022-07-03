#!/usr/bin/python3

def titleToNumber(columnTitle):
    result = 0
    for s in columnTitle:
        result = result * 26 + s.encode('ascii')[0] - 64
    return result

print(titleToNumber('A'))
print(titleToNumber('AB'))

