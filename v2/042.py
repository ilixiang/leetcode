#!/usr/bin/python3

def trap(height):
    if len(height) <= 2:
        return 0

    left = 0
    right = len(height) - 1

    leftHeight = height[left]
    rightHeight = height[right]

    water = min(height[left], height[right]) * (right - left - 1)
    while left < right:
        if height[left] <= height[right]:
            left += 1
            while left < right and height[left] <= leftHeight:
                water -= height[left]
                left += 1
            if left < right:
                water -= leftHeight
                water += (min(height[left], rightHeight) - leftHeight) * (right - left - 1)
                leftHeight = height[left]
        else:
            right -= 1
            while left < right and height[right] <= rightHeight:
                water -= height[right]
                right -= 1
            if left < right:
                water -= rightHeight
                water += (min(leftHeight, height[right]) - rightHeight) * (right - left - 1)
                rightHeight = height[right]
    return water

