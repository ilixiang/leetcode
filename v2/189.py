#!/usr/bin/python3

def rotate(nums, k):
    m = len(nums)
    k %= m
    if k == 0:
        return

    def reverse(i, j):
        left, right = i, j - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    reverse(0, m - k)
    reverse(m - k, m)
    reverse(0, m)

