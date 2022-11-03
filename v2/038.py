#!/usr/bin/python3

def countAndSay(n):
    if n == 1:
        return '1'
    
    prevRes = countAndSay(n - 1)
    tmp = []

    i = 0
    count = 1
    while i < len(prevRes):
        while i + 1 < len(prevRes) and prevRes[i] == prevRes[i + 1]:
            count += 1
            i += 1
        tmp.append(str(count))
        tmp.append(prevRes[i])
        count = 1
        i += 1
    return ''.join(tmp)
