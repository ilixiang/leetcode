#!/usr/bin/python3

def maximalRectangle(matrix):
    m, n = len(matrix), len(matrix[0])
    rev, histogram = 0, [0] * n

    def largestRectangleArea(heights):
        rev, length, stack = 0, len(heights), []
        for i in range(length + 1):
            while len(stack) != 0 and (i == length or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                left, right = 0 if len(stack) == 0 else (stack[-1] + 1), i
                rev = max(rev, height * (right - left))
            stack.append(i)
        return rev

    for i in range(m):
        for j in range(n):
            histogram[j] = 0 if matrix[i][j] == '0' else (histogram[j] + 1)
        rev = max(rev, largestRectangleArea(histogram))
    return rev
