#!/usr/bin/python3

def threeSum(nums):
    nums.sort()
    
    rev = []
    l = 0
    while l < len(nums) - 2:
        if l != 0 and nums[l] == nums[l - 1]:
            l += 1
            continue
        diff = 0 - nums[l]
        m, r = l + 1, len(nums) - 1
        while m < r:
            s = nums[m] + nums[r]
            if s == diff:
                rev.append([nums[l], nums[m], nums[r]])
                m += 1
                while m < r and nums[m] == nums[m - 1]:
                    m += 1
            elif s < diff:
                m += 1
            else:
                r -= 1
        l += 1
    return rev
            
