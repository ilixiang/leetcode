#!/usr/bin/python3

def permute(nums):
    if len(nums) == 1:
        return [nums]
    used = 0
    tmp = [None] * len(nums)
    res = []
    permuteRecursive(nums, 0, used, tmp, res)
    return res

def permuteRecursive(nums, current, used, tmp, res):
    if current == len(nums):
        res.append(list(tmp))
        return

    for i in range(0, len(nums)):
        if used & (1 << i) != 0:
            continue
        used |= 1 << i
        tmp[current] = nums[i]
        permuteRecursive(nums, current, used, tmp, res)
        used &= ~(1 << i)
