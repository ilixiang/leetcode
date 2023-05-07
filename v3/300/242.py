#!/usr/bin/python3

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sMap = {}
    for c in s:
        sMap[c] = sMap.get(c, 0) + 1
    
    for c in t:
        tCount = sMap.get(c, 0)
        if tCount == 0:
            return False
        sMap[c] = tCount - 1
    return True
