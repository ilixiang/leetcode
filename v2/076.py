#!/usr/bin/python3

def minWindow(s, t):
    sLen = len(s)
    tLen = len(t)
    if tLen > sLen:
        return ''
    
    m = {}
    for tc in t:
        if not tc in m:
            m[tc] = 1
        else:
            m[tc] += 1
    distinctCharCount = len(m)
    
    left, right = 0, 0
    res = ''
    while right < len(s):
        c = s[right]
        if c in m:
            m[c] -= 1
            if m[c] == 0:
                distinctCharCount -= 1
                if distinctCharCount == 0:
                    while left <= right:
                        lc = s[left]
                        if lc in m:
                            m[lc] += 1
                            if m[lc] == 1:
                                res = s[left: right + 1] if (res == '' or len(res) > (right - left + 1)) else res
                                left += 1
                                distinctCharCount += 1
                                break
                        left += 1
        right += 1

