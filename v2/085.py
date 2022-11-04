#!/usr/bin/python3

def maximalRectangle(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rev = 0
    nums = [0] * n
    for row in range(0, m):
        for col in range(0, n):
            if matrix[row][col] == '0':
                nums[col] = 0
            else:
                nums[col] += 1
        stack = []
        for col in range(0, n):
            while len(stack) != 0 and nums[stack[len(stack) - 1]] > nums[col]:
                height = nums[stack.pop()]
                left = -1 if len(stack) == 0 else stack[len(stack) - 1]
                rev = max(rev, height * (col - left - 1))
            stack.append(col)
        while len(stack) != 0:
            height = nums[stack.pop()]
            left = -1 if len(stack) == 0 else stack[len(stack) - 1]
            rev = max(rev, height * (n - left - 1))
    return rev
