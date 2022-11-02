#!/usr/bin/python3

def trap(heights):
    if len(heights) < 2:
        return 0
    previousMinHeight = 0
    left = 0
    right = len(heights) - 1
    water = 0
    while left < right:
        print('LEFT => %d, RIGHT => %d, WATER => %d'%(left, right, water))
        minHeight = min(heights[left], heights[right])
        maxHeight = max(heights[left], heights[right])
        if minHeight > previousMinHeight:
            water = water + (minHeight - previousMinHeight) * (right - left) - minHeight
            previousMinHeight = minHeight
        else:
            water = water - minHeight
        if heights[left] < heights[right]:
            left = left + 1
        else:
            right = right - 1
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

