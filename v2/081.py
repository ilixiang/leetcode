#!/usr/bin/python3

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] == nums[right]:
            if nums[left] == target:
                return True
            else:
                left += 1
                right -= 1
                continue

        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        
        if nums[mid] <= nums[right]:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return False
