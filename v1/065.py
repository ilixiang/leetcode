#!/usr/bin/python3

def isNumber(s):
    index = 0
    length = len(s)
    while index < len(s) and (s[index] == '+' or s[index] == '-'):
        index = index + 1
    signRange = (0, index)
    if signRange[1] != 0 and signRange[1] != 1:
        return False

    while index < len(s) and (s[index] != 'E' and s[index] != 'e'):
        index = index + 1
    decimalRange = (signRange[1], index)
    exponentRange = (index, length)

    if decimalRange[1] <= decimalRange[0]:
        return False
    hasDot = False
    for index in range(decimalRange[0], decimalRange[1]):
        if s[index] == '.':
            if hasDot:
                return False
            else:
                hasDot = True
                continue
        if s[index] > '9' or s[index] < '0':
            return False
    if hasDot and decimalRange[1] - decimalRange[0] == 1:
        return False

    if exponentRange[0] == exponentRange[1]:
        return True

    index = exponentRange[0] + 1
    while index < length and (s[index] == '+' or s[index] == '-'):
        index = index + 1
    exponentSignRange = (exponentRange[0] + 1, index)
    if exponentSignRange[1] - exponentSignRange[0] != 0 and exponentSignRange[1] - exponentSignRange[0] != 1:
        return False

    exponentIntegerRange = (index, length)
    if exponentIntegerRange[0] == exponentIntegerRange[1]:
        return False
    for index in range(exponentIntegerRange[0], exponentIntegerRange[1]):
        if s[index] < '0' or s[index] > '9':
            return False
    return True

print(isNumber('2'))
print(isNumber('0089'))
print(isNumber('-0.1'))
print(isNumber('+3.14'))
print(isNumber('4.'))
print(isNumber('-.9'))
print(isNumber('2e10'))
print(isNumber('-90E3'))
print(isNumber('3e+7'))
print(isNumber('+6e-1'))
print(isNumber('53.5e93'))
print(isNumber('-123.456e789'))

print(isNumber('abc'))
print(isNumber('1a'))
print(isNumber('1e'))
print(isNumber('e3'))
print(isNumber('99e2.5'))
print(isNumber('--6'))
print(isNumber('+-3'))
print(isNumber('95a54e53'))
