#!/usr/bin/python3

def addBinary(a, b):
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    tmp = []
    while i >= 0 and j >= 0:
        s = int(a[i]) + int(b[j]) + carry
        tmp.append(str(s & 1))
        carry = s >> 1
        i -= 1
        j -= 1
    
    while i >= 0:
        s = int(a[i]) + carry
        tmp.append(str(s & 1))
        carry = s >> 1
        i -= 1
    
    while j >= 0:
        s = int(b[j]) + carry
        tmp.append(str(s & 1))
        carry = s >> 1
        j -= 1
    
    if carry != 0:
        tmp.append(str(carry))
    tmp.reverse()
    return ''.join(tmp)
