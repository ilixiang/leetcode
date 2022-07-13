#!/usr/bin/python3

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    sMap = {}
    for sChar in s:
        if not sChar in sMap:
            sMap[sChar] = 0
        sMap[sChar] += 1

    for tChar in t:
        if not tChar in sMap or sMap[tChar] == 0:
            return False
        sMap[tChar] -= 1
    return True

