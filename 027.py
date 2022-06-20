#!/usr/bin/python3

def removeElement(nums, val):
    limit = 0
    for index in range(0, len(nums)):
        if nums[index] != val:
            nums[limit] = nums[index]
            limit = limit + 1
    return limit

print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

