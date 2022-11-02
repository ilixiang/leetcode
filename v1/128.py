#!/usr/bin/python3

def longestConsecutive(nums):
    numSet = set(nums)

    maxLength = 0
    for num in numSet:
        if not num - 1 in numSet:
            currentLength = 1
            while num + 1 in numSet:
                num = num + 1
                currentLength = currentLength + 1
            maxLength = max(maxLength, currentLength)
    return maxLength

print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


