#!/usr/bin/python3

def search(nums, target):
    low, high = 0, len(nums)
    mid = (low + high) // 2
    while low < high:
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            if nums[low] == target:
                return low
            elif nums[low] < target or (nums[mid] <= nums[high - 1]):
                high = mid
            else:
                low = mid + 1
        else:
            if nums[high - 1] == target:
                return high - 1
            if target < nums[high - 1] or (nums[low] <= nums[mid]):
                low = mid + 1
            else:
                high = mid
        mid = (low + high) // 2
    return -1

print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))
print(search([1, 3], 1))
print(search([3, 1], 3))
print(search([7, 8, 1, 2, 3, 4, 5, 6], 2))

