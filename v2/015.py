#!/usr/bin/python3

def threeSum(nums): 
    nums.sort()
    res = []
    i = 0
    while i < (len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        target = -1 * nums[i]
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        i += 1
        while i < (len(nums) - 2) and nums[i] == nums[i - 1]:
            i += 1
    return res

