#!/usr/bin/python3

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[right] < nums[left]:
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
        else:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

if __name__ == '__main__':
    assert search([3, 5, 1], 3) == 0
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4