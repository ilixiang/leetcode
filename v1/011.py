#!/usr/bin/python3

def maxArea(heights):
    if len(heights) == 0:
        return 0

    left = 0
    right = len(heights) - 1
    area = 0
    while left < right:
        area = max(area, (right - left) * min(heights[left], heights[right])) 
        if heights[left] < heights[right]:
            originalLeft = left
            left = left + 1
            while heights[left] < heights[originalLeft] and left < right:
                left = left + 1
        else:
            originalRight = right
            right = right - 1
            while heights[right] < heights[originalRight] and left < right:
                right = right - 1
    return area

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

