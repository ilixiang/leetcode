#!/usr/bin/python3

def finMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[left] < nums[right]:
            return nums[left]
        elif nums[left] > nums[right]:
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                while left < right and nums[left] == nums[right]:
                    left += 1
                if left == right:
                    return nums[left]
    return nums[(left + right) >> 1]
