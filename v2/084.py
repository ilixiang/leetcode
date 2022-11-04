#!/usr/bin/python3

def largestRectangleArea(heights):
    size = len(heights)
    if size == 0:
        return 0

    stack = []

    rev = 0
    for i in range(0, size):
        while len(stack) != 0 and heights[stack[len(stack) - 1]] > heights[i]:
            height = heights[stack.pop()]
            left = -1 if len(stack) == 0 else stack[len(stack) - 1]
            rev = max(rev, (i - left - 1) * height)
        stack.append(i)
    while len(stack) != 0:
        height = heights[stack.pop()]
        left = -1 if len(stack) == 0 else stack[len(stack) - 1]
        rev = max(rev, (size - left - 1) * height)
    return rev

