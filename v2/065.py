#!/usr/bin/python3

def isNumber(s):
    i = 0
    
    if s[i] == '-' or s[i] == '+':
        i += 1
    
    integerStart = i
    while i < len(s) and s[i].isdecimal():
        i += 1
    integerEnd = i
    integerExist = integerEnd != integerStart

    decimalExist = False
    if i < len(s) and s[i] == '.':
        i += 1
        decimalStart = i
        while i < len(s) and s[i].isdecimal():
            i += 1
        decimalEnd = i
        decimalExist = decimalEnd != decimalStart
        
    if not integerExist and not decimalExist:
        return False
    
    if i < len(s) and (s[i] == 'E' or s[i] == 'e'):
        i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            i += 1
        exponentStart = i
        while i < len(s) and s[i].isdecimal():
            i += 1
        exponentEnd = i
        if exponentEnd == exponentStart:
            return False
    
    return i == len(s)
