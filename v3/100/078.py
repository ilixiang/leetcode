#!/usr/bin/python3

def subsets(nums):
    length, rev = len(nums), []
    def combineRecursive(start, pos, tmp, n):
        if pos == n:
            rev.append(list(tmp))
            return
        for i in range(start, length + 1 - n + pos):
            tmp[pos] = nums[i]
            combineRecursive(i + 1, pos + 1, tmp, n)

    for n in range(len(nums)):
        tmp = [0] * n
        combineRecursive(0, 0, tmp, n)
    rev.append(list(nums))
    return rev
