#!/usr/bin/python3

def getPermutation(n, k):
    if n == 1:
        return '1'

    k -= 1
    used = 0
    fac = [1] * n
    for i in range(2, n):
        fac[i] = i * fac[i - 1]
    
    tmp = [None] * n
    for i in range(0, n):
        nextPosibilityNum = fac[n - 1 - i]
        sequence = k // nextPosibilityNum
        k = k % nextPosibilityNum
        positionNum = 0
        while sequence >= 0:
            positionNum += 1
            if used & (1 << positionNum) == 0:
                sequence -= 1
        used |= 1 << positionNum
        tmp[i] = str(positionNum)
    return ''.join(tmp)
