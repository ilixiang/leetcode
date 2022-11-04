#!/usr/bin/python3

def subsetsWithDup(nums):
    nums.sort()
    n = len(nums)
    res = []
    for k in range(0, len(nums) + 1):
        tmp = [None] * k
        combinationRecurisve(nums, n, k, 0, 0, tmp, res)
    return res

def combinationRecurisve(nums, n, k, cur, start, tmp, res):
    if cur == k:
        res.append(list(tmp))
        return
    
    i = start
    end = n - (k - 1 - cur)
    while i < end:
        if i != start and nums[i] == nums[i - 1]:
            i += 1
            continue
        tmp[cur] = nums[i]
        combinationRecurisve(nums, n, k, cur + 1, i + 1, tmp, res)
        i += 1
