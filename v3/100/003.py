#!/usr/bin/python3

def lengthOfLongestSubstring(s):
    m = {}

    l = rev = 0
    for r in range(len(s)):
        c = s[r]
        cIndex = m.get(c, None)
        if cIndex != None and l <= cIndex:
            rev = max(rev, r - l)
            l = cIndex + 1
        m[c] = r

    rev = max(rev, len(s) - l)
    return rev
