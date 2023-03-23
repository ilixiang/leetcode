#!/usr/bin/python3

def combine(n, k):
    rev = []
    tmp = [0] * k
    def combineRecursive(start, pos):
        if pos == k:
            rev.append(list(tmp))
            return
        
        for i in range(start, n + 1 - k + pos):
            tmp[pos] = i + 1
            combineRecursive(i + 1, pos + 1)
    
    combineRecursive(0, 0)
    return rev
