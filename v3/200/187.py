#!/usr/bin/python3

def findRepeatDnaSequences(s):
    m = {}
    for i in range(len(s) - 9):
        ss = s[i:i + 10]
        m[ss] = m.get(ss, 0) + 1
    
    rev = []
    for k in m:
        if m[k] > 1:
            rev.append(k)
    return rev
