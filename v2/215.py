#!/usr/bin/python3

import random

def findKthLargest(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        randPivotIndex = random.randint(left, right)
        nums[right], nums[randPivotIndex] = nums[randPivotIndex], nums[right]
        pivot = nums[right]
        divider = left - 1
        for i in range(left, right):
            num = nums[i]
            if num < pivot:
                divider += 1
                nums[divider], nums[i] = nums[i], nums[divider]
        divider += 1
        nums[divider], nums[right] = nums[right], nums[divider]

        if divider == len(nums) - k:
            return nums[divider]
        elif divider < len(nums) - k:
            left = divider + 1
        else:
            right = divider - 1
    return None
