#!/usr/bin/python3

def findMin(nums):
    low, high = 0, len(nums)
    mid = (low + high) // 2
    while low < high:
        if nums[low] == nums[mid]:
            return nums[low]
        elif nums[low] < nums[mid]:
            if nums[low] <= nums[high - 1]:
                return nums[low]
            else:
                low = mid
        else:
            if nums[mid] >= nums[high - 1]:
                return nums[high - 1]
            else:
                high = mid + 1
        mid = (low + high) // 2
    return nums[mid]
            
print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([11, 13, 15, 17]))
print(findMin([2, 1]))

