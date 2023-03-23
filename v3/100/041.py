#!/usr/bin/python3

def firstMissingPositive(nums):
    for i in range(len(nums)):
        if nums[i] > 0 and nums[i] <= len(nums):
            nums[i] -= 1
        else:
            nums[i] = -1
    
    for i in range(len(nums)):
        num = nums[i]
        while num != i and num != -1 and nums[num] != num:
            tmp = nums[num]
            nums[num] = num
            num = tmp
        nums[i] = num

    i = 0
    while i < len(nums) and nums[i] == i:
        i += 1
    return i + 1

if __name__ == '__main__':
    assert firstMissingPositive([1, 2, 0]) == 3
    assert firstMissingPositive([3, 4, -1, 1]) == 2
