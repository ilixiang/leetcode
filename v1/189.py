#!/usr/bin/python3

def rotate(nums, k):
    length = len(nums)
    remainder = k % length
    rank = length
    while remainder != 0:
        tmp = remainder
        remainder = rank % remainder
        rank = tmp

    for i in range(0, rank):
        currentVal = nums[i]
        nextIndex = (i + k) % length
        while nextIndex != i:
            tmp = nums[nextIndex]
            nums[nextIndex] = currentVal
            currentVal = tmp
            nextIndex = (nextIndex + k) % length
        nums[nextIndex] = currentVal

def rotateByReverse(nums, k):
    length = len(nums)
    k = k % length
    reverse(nums, 0, length - k - 1)
    print(nums)
    reverse(nums, length - k, length - 1)
    print(nums)
    reverse(nums, 0, length - 1)
    print(nums)

def reverse(nums, low, high):
    while low < high:
        tmp = nums[low]
        nums[low] = nums[high]
        nums[high] = tmp
        low = low + 1
        high = high - 1

nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)
nums = [1, 2, 3, 4, 5, 6, 7]
rotateByReverse(nums, 3)
print(nums)

