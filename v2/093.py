#!/usr/bin/python3

def restoreIpAddress(s):
    tmp = [None] * 4
    res = []
    restoreIpAddressRecursive(s, 0, 0, tmp, res)
    return res

def restoreIpAddressRecursive(s, n, i, tmp, res):
    if n == 4 and i == len(s):
        res.append('.'.join(tmp))
        return
    
    if n == 4 or i == len(s):
        return
    
    if s[i] == '0':
        tmp[n] = '0'
        restoreIpAddressRecursive(s, n + 1, i + 1, tmp, res)
        return
    
    j = i + 1
    while j <= len(s):
        part = s[i:j]
        if int(part) <= 255:
            tmp[n] = part
            restoreIpAddressRecursive(s, n + 1, j, tmp, res)
        j += 1
