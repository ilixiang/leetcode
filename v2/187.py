#!/usr/bin/python3

def findRepeatedDnaSequences(s):
    m = {}
    rev = []
    for i in range(0, len(s) - 10 + 1):
        ss = s[i: i + 10]
        if not ss in m:
            m[ss] = 1
        else:
            m[ss] += 1
            if m[ss] == 2:
                rev.append(ss)
    return rev
