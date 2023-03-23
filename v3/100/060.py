#!/usr/bin/python3

def getPermutation(n, k):
    k -= 1
    tmp = []
    nums = [i for i in range(1, n + 1)]
    posibility = 1
    for i in range(1, n):
        posibility *= i
    while k != 0:
        pos = k // posibility
        tmp.append(nums[pos])
        del nums[pos]
        k %= posibility
        posibility //= (n - 1)
        n -= 1
    tmp.extend(nums)
    return ''.join(map(lambda e: str(e), tmp))