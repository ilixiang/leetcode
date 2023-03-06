#!/usr/bin/python3

def minWindow(s, t):
    if len(s) < len(t):
        return ''

    m = {}
    for c in t:
        m[c] = m.get(c, 0) + 1

    remain = len(t)
    l = r = 0
    indexTuple = (-1, len(s))
    while r < len(s) or remain == 0:
        # move right pointer
        if remain != 0:
            c = s[r]
            cRemain = m.get(c, None)
            if cRemain != None:
                m[c] = cRemain - 1
                if cRemain > 0:
                    remain -= 1
            r += 1
        # move left pointer
        else:
            c = s[l]
            cRemain = m.get(c, None)
            if cRemain != None:
                m[c] = cRemain + 1
                if cRemain >= 0:
                    remain += 1
                if r - l < indexTuple[1] - indexTuple[0]:
                    indexTuple = (l, r)
            l += 1
    (l, r) = indexTuple
    return '' if l == -1 else s[l:r]
