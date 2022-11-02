#!/usr/bin/python3

def summaryRanges(nums):
    if len(nums) == 0:
        return []

    length = len(nums)
    result = []
    start = 0
    current = 0
    while current < length:
        start = current
        while current < length and (current == start or nums[current] == nums[current - 1] + 1):
            current += 1
        result.append(str(nums[start]) if current == start + 1 else (str(nums[start]) + '->' + str(nums[current - 1])))
    return result

print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))


