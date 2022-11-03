#!/usr/bin/python3

def permuteUnique(nums):
    if len(nums) == 1:
        return [nums]

    nums.sort()
    used = 0
    tmp = [None] * len(nums)
    res = []
    permuteUniqueRecursive(nums, 0, used, tmp, res)
    return res
    
def permuteUniqueRecursive(nums, current, used, tmp, res):
    if current == len(nums):
        res.append(list(tmp))
        return
    
    i = 0
    s = set()
    while i < len(nums):
        if used & (1 << i) == 0 and not nums[i] in s:
            used |= (1 << i)
            tmp[current] = nums[i]
            permuteUniqueRecursive(nums, current + 1, used, tmp, res)
            used &= ~(1 << i)
            s.add(nums[i])
        i += 1
