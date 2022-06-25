#!/usr/bin/python3

def removeDuplicates(nums):
    left = -1
    firstSameIndex = 0
    index = 0
    while index < len(nums):
        if nums[index] != nums[firstSameIndex]:
            firstSameIndex = index
        if index - firstSameIndex < 2:
            nums[left + 1] = nums[index]
            left = left + 1
        index = index + 1
    return left + 1

print(removeDuplicates([1, 1, 1, 2, 2, 3]))

