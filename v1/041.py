#!/usr/bin/python3

def firstMissingPositive(nums):
    for index in range(0, len(nums)):
        nums[index] = nums[index] - 1
    for index in range(0, len(nums)):
        num = nums[index]
        while num >= 0 and num < len(nums) and num != index and num != nums[num]:
            tmp = nums[num]
            nums[num] = num
            num = tmp
        nums[index] = num
    for index in range(0, len(nums)):
        if index != nums[index]:
            return index + 1
    return len(nums) + 1

print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8 ,9, 11, 12]))
print(firstMissingPositive([1, 1]))

