#!/usr/bin/python3

def addBinary(a, b):
    tmp = []
    c = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 and j >= 0:
        s = int(a[i]) + int(b[j]) + c
        tmp.append(s % 2)
        c = s // 2
        i -= 1
        j -= 1
    
    while i >= 0:
        s = int(a[i]) + c
        tmp.append(s % 2)
        c = s // 2
        i -= 1
    while j >= 0:
        s = int(b[j]) + c
        tmp.append(s % 2)
        c = s // 2
        j -= 1
    if c != 0:
        tmp.append(c)
    return ''.join(map(lambda e: str(e), reversed(tmp)))