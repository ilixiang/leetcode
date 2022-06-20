#!/usr/bin/python3

def permute(nums):
    if len(nums) == 0:
        return []
    useds = [False] * len(nums)
    indexStack = []
    result = []
    nextPermute(nums, indexStack, useds, result)
    return result

def nextPermute(nums, indexStack, useds, result):
    if len(indexStack) == len(nums):
        result.append(list(map(lambda i: nums[i], indexStack)))
        return

    for index in range(0, len(nums)):
        if not useds[index]:
            useds[index] = True
            indexStack.append(index)
            nextPermute(nums, indexStack, useds, result)
            indexStack.pop()
            useds[index] = False

print(permute([1, 2, 3,]))

