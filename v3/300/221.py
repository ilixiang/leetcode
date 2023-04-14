#!/usr/bin/python3

def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    nums = [0] * n
    rev = 0
    stack = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '0':
                nums[j] = 0
            else:
                nums[j] += 1
        
        for j in range(n):
            while len(stack) != 0 and nums[stack[-1]] >= nums[j]:
                x = stack.pop()
                if nums[x] > rev:
                    rev = max(rev, min(nums[x], (j - stack[-1] - 1) if len(stack) != 0 else j))
            stack.append(j)
        while len(stack) != 0:
            x = stack.pop()
            if nums[x] > rev:
                rev = max(rev, min(nums[x], (len(nums) - stack[-1] - 1) if len(stack) != 0 else len(nums)))
    return rev ** 2
