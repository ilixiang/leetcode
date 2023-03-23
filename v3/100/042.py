#!/usr/bin/python3

def trap(height):
    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]
    rev = 0
    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(height[left], maxLeft)
            rev += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(height[right], maxRight)
            rev += maxRight - height[right]
    return rev
