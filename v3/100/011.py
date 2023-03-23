#!/usr/bin/python3

def maxArea(height):
    l, r = 0, len(height) - 1
    rev = 0
    while l < r:
        tmp = (r - l) * min(height[l], height[r])
        rev = max(rev, tmp)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return rev
