#!/usr/bin/python3

def summaryRanges(nums):
    if len(nums) == 0:
        return []

    rev = []
    left, right = 0, 1
    while right < len(nums):
        if nums[right] != nums[right - 1] + 1:
            if left == right - 1:
                rev.append(str(nums[left]))
            else:
                rev.append(str(nums[left]) + '->' + str(nums[right - 1]))
            left = right
        right += 1
    if left == right - 1:
        rev.append(str(nums[left]))
    else:
        rev.append(str(nums[left]) + '->' + str(nums[right - 1]))
    return rev
    

