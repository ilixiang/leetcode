#!/usr/bin/python3

def subsets(nums):
    res = []
    length = len(nums)
    for size in range(0, len(nums) + 1):
        tmp = [None] * size
        combinationRecursive(nums, length, size, 0, 0, tmp, res)
    return res

def combinationRecursive(nums, n, k, cur, start, tmp, res):
    if cur == k:
        res.append(list(map(lambda i: nums[i], tmp)))
        return
    
    for i in range(start, n - (k - 1 - cur)):
        tmp[cur] = i
        combinationRecursive(nums, n, k, cur + 1, i + 1, tmp, res)
