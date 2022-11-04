#!/usr/bin/python3

def combine(n, k):
    tmp = [None] * k
    res = []
    combineRecursive(n, k, 0, 1, tmp, res)
    return res

def combineRecursive(n, k, cur, start, tmp, res):
    if cur == k:
        res.append(list(tmp))
        return
    
    for i in range(start, n - (k - 1 - cur) + 1):
        tmp[cur] = i
        combineRecursive(n, k, cur + 1, i + 1, tmp, res)
