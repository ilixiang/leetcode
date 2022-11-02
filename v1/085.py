#!/usr/bin/python3

def maximalRectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rev = 0
    histogram = [0] * cols
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == '0':
                histogram[j] = 0
            else:
                histogram[j] += 1
        print(histogram)
        rev = max(rev, largestRectangleArea(histogram))
    return rev

def largestRectangleArea(heights):
    s = []
    rightMins = [None] * len(heights)

    rev = 0

    for i in range(0, len(heights)):
        height = heights[i]
        while len(s) != 0 and heights[s[len(s) - 1]] > height:
            rightMins[s.pop()] = i
        s.append(i)

    s.clear()
    for i in range(len(heights) - 1, -1, -1):
        height = heights[i]
        while len(s) != 0 and heights[s[len(s) - 1]] > height:
            cur = s.pop()
            left = i
            right = len(heights) if rightMins[cur] == None else rightMins[cur]
            rev = max(rev, heights[cur] * (right - left - 1))
        s.append(i)

    for cur in s:
        right = len(heights) if rightMins[cur] == None else rightMins[cur]
        rev = max(rev, heights[cur] * right)
    return rev


print(maximalRectangle([['0', '1'], ['1', '0']]))
