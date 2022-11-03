#!/usr/bin/python3

def groupAnagrams(strs):
    m = {}
    for s in strs:
        l = list(s)
        l.sort()
        ss = ''.join(l)
        if not ss in m:
            m[ss] = []
        m[ss].append(s)
    res = []
    for k in m:
        res.append(m[k])
    
    return res

