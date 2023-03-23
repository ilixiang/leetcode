#!/usr/bin/python3

def countAndSay(n):
    if n == 1:
        return '1'
    prevRev = countAndSay(n - 1)

    mem = []
    count = 1
    i = 0
    while i < len(prevRev):
        if i != len(prevRev) - 1 and prevRev[i] == prevRev[i + 1]:
            count += 1
            i += 1
            continue
        mem.append(str(count) + prevRev[i])
        count = 1
        i += 1
    return ''.join(mem)
