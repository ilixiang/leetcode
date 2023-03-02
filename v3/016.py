#!/usr/bin/python3

def threeSumClosest(nums, target):
    nums.sort()

    l = 0
    biggest = sum(nums[-3:])
    if target >= biggest:
        return biggest
    
    smallest = sum(nums[:3])
    if target <= smallest:
        return smallest

    rev = smallest
    while l < len(nums) - 2:
        if l != 0 and nums[l] == nums[l - 1]:
            l += 1
            continue
        m, r = l + 1, len(nums) - 1
        while m < r:
            s = nums[l] + nums[m] + nums[r]

            if abs(s - target) < abs(rev - target):
                rev = s
            
            if s == target:
                return target
            elif s < target:
                m += 1
            else:
                r -= 1
        l += 1
    return rev
