#!/usr/bin/python3

import random

def findKthLargest(nums, k):
    def partition(left, right):
        rand = random.randint(left, right)
        nums[rand], nums[right] = nums[right], nums[rand]
        cur = delimiter = left
        while cur < right:
            if nums[cur] <= nums[right]:
                nums[delimiter], nums[cur] = nums[cur], nums[delimiter]
                delimiter += 1
            cur += 1
        nums[right], nums[delimiter] = nums[delimiter], nums[right]
        return delimiter
    target = len(nums) - k
    left, right = 0, len(nums) - 1
    delimiter = partition(left, right)
    while delimiter != target:
        if delimiter > target:
            right = delimiter - 1
        else:
            left = delimiter + 1
        delimiter = partition(left, right)
    return nums[delimiter]
