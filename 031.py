#!/usr/bin/python3

def nextPermutation(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    
    swapIndex = -1
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            swapIndex = i - 1
            break
    print(swapIndex)
    
    if swapIndex != -1:
        otherIndex = -1
        for i in range(swapIndex + 1, len(nums) - 1):
            if nums[i] > nums[swapIndex] and nums[i + 1] <= nums[swapIndex]:
                otherIndex = i
        otherIndex = len(nums) - 1 if otherIndex == -1 else otherIndex
        tmp = nums[swapIndex]
        nums[swapIndex] = nums[otherIndex]
        nums[otherIndex] = tmp
    
    left, right = swapIndex + 1, len(nums) - 1
    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left = left + 1
        right = right - 1

a = [1, 5, 1]
nextPermutation(a)
print(a)
