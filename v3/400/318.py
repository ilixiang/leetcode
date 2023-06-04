#!/usr/bin/python3

def maxProduct(words):
    m = len(words)
    a = [0] * m
    for i in range(m):
        word = words[i]
        for c in set(list(word)):
            a[i] |= 1 << (ord(c) - 97)
    
    rev = 0
    for i in range(m):
        for j in range(i + 1, m):
            if a[i] & a[j] == 0:
                rev = max(rev, len(words[i]) * len(words[j]))
    return rev
    