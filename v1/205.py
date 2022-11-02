#!/usr/bin/python3

def isIsomorphic(s, t):
    sMap = {}
    tMap = {}
    for i in range(0, len(s)):
        sChar = s[i]
        tChar = t[i]
        if sMap.get(sChar) != tMap.get(tChar):
            return False
        sMap[sChar] = i
        tMap[tChar] = i
    return True

print(isIsomorphic('egg', 'add'))
print(isIsomorphic('foo', 'bar'))

