#!/usr/bin/python3

def rotate(nums, k):
    m = len(nums)
    k %= m
    if k == 0:
        return
    
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    reverse(0, m - k - 1)
    reverse(m - k, m - 1)
    reverse(0, m - 1)
