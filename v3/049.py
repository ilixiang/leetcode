#!/usr/bin/python3

def groupAnagrams(strs):
    m = {}
    for s in strs:
        key = ''.join(sorted(list(s)))
        a = m.get(key, None)
        if a == None:
            a = []
            m[key] = a
        a.append(s)
    
    rev = []
    for v in m.values():
        rev.append(v)
    return rev
