#!/usr/bin/python3

def permuteUnique(nums):
    if len(nums) == 0:
        return []
    indexStack = []
    useds = [False] * len(nums)
    result = []
    nextPermuteUnique(nums, indexStack, useds, result)
    return result

def nextPermuteUnique(nums, indexStack, useds, result):
    if len(indexStack) == len(nums):
        result.append(list(map(lambda i: nums[i], indexStack)))
        return

    consumedNumSet = set()
    for index in range(0, len(nums)):
        if not useds[index] and not nums[index] in consumedNumSet:
            useds[index] = True
            indexStack.append(index)
            nextPermuteUnique(nums, indexStack, useds, result)
            useds[index] = False
            indexStack.pop()
            consumedNumSet.add(nums[index])

print(permuteUnique([1,1,2]))

