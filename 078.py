#!/usr/bin/python3

def subsets(nums):
    indices = []
    result = [[]]
    for i in range(1, len(nums) + 1):
        combineRecursive(nums, i, 0, indices, result)
    return result

def combineRecursive(nums, remain, start, indices, result):
    if remain == 0:
        result.append(list(map(lambda i: nums[i], indices)))
        return

    for i in range(start, len(nums) - remain + 1):
        indices.append(i)
        combineRecursive(nums, remain - 1, i + 1, indices, result)
        indices.pop()

print(subsets([1, 2, 3]))

