#!/usr/bin/python3

def maxArea(height):
    if len(height) <= 1:
        return 0
    
    left = 0
    right = len(height) - 1
    res = min(height[left], height[right]) * (right - left)
    while left < right:
        if height[left] < height[right]:
            curHeight = height[left]
            while left < right and height[left] <= curHeight:
                left += 1
        else:
            curHeight = height[right]
            while left < right and height[right] <= curHeight:
                right -= 1
        res = max(res, min(height[left], height[right]) * (right - left))
    return res
