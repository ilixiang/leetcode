#!/usr/bin/python3

def largestRectangleArea(heights):
    rev, length, stack = 0, len(heights), []
    for i in range(length + 1):
        while len(stack) != 0 and (i == length or heights[stack[-1]] > heights[i]):
            height = heights[stack.pop()]
            left, right = 0 if len(stack) == 0 else (stack[-1] + 1), i
            rev = max(rev, height * (right - left))
        stack.append(i)
    return rev
