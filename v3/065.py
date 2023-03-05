#!/usr/bin/python3

def isNumber(s):
    if len(s) == 0:
        return False

    l = 0
    if s[l] == '+' or s[l] == '-':
        l += 1

    r = l
    while r < len(s) and s[r].isdigit():
        r += 1
    integerPartLen = r - l

    hasDot = False
    if r < len(s) and s[r] == '.':
        hasDot = True
        r += 1
    
    l = r
    while r < len(s) and s[r].isdigit():
        r += 1
    fractionPartLen = r - l
    if (not hasDot and integerPartLen == 0)\
        or (hasDot and (integerPartLen == 0 and fractionPartLen == 0)):
        return False
    
    if r == len(s):
        return True
    
    if s[r] != 'E' and s[r] != 'e':
        return False

    r += 1
    if r == len(s):
        return False
    if s[r] == '+' or s[r] == '-':
        r += 1

    l = r
    while r < len(s) and s[r].isdigit():
        r += 1
    return r == len(s) and r - l != 0
