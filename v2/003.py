#!/usr/bin/python3

def lengthOfLongestSubstring(s):
    m = {}
    res = 0
    start = 0
    for i in range(0, len(s)):
        c = s[i]
        if c in m:
            prevIndex = m[c]
            if prevIndex >= start:
                res = max(res, i - start)
                start = prevIndex + 1
        m[c] = i
    res = max(res, len(s) - start)
    return res
