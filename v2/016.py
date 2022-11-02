#!/usr/bin/python3

def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    left = 0
    while left < (len(nums) - 2):
        mid = left + 1
        right = len(nums) - 1
        while mid < right:
            s = nums[left] + nums[mid] + nums[right]
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                mid += 1
            elif s > target:
                right -= 1
            else:
                return s
        left += 1
    return res

