#!/usr/bin/python3

def search(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] >= nums[left]:
                    if target <= nums[right] or target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target >= nums[left] or target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1
