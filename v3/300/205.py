#!/usr/bin/python3

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    m = len(s)
    stMap = {}
    tsMap = {}
    
    i = 0
    while i < m:
        sc, tc = s[i], t[i]
        stMapping = stMap.get(sc, None)
        tsMapping = tsMap.get(tc, None)
        if stMapping == None and tsMapping == None:
            stMap[sc] = tc
            tsMap[tc] = sc
        elif stMapping == None or tsMapping == None:
            return False
        else:
            if stMapping != tc or tsMapping != sc:
                return False
        i += 1
    return True

