#!/usr/bin/python3

def subsetsWithDup(nums):
    nums.sort()
    tmp = []
    result = [[]]
    for i in range(1, len(nums) + 1):
        subsetsWithDupRecursive(nums, i, 0, tmp, result)
    return result

def subsetsWithDupRecursive(nums, remains, start, tmp, result):
    if remains == 0:
        result.append(list(tmp))
        return

    index = start
    while index <= len(nums) - remains:
        tmp.append(nums[index])
        subsetsWithDupRecursive(nums, remains - 1, index + 1, tmp, result)
        tmp.pop()
        while index + 1 <= len(nums) - remains and nums[index + 1] == nums[index]:
            index = index + 1
        index = index + 1

print(subsetsWithDup([1, 2, 2]))

