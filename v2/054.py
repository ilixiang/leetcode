#!/usr/bin/python3

def spiralOrder(matrix):
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    res = [None] * (right + 1) * (bottom + 1)
    cur = 0
    while left < right and top < bottom:
        for x in range(left, right):
            res[cur] = matrix[top][x]
            cur += 1
        for y in range(top, bottom):
            res[cur] = matrix[y][right]
            cur += 1
        for x in range(right, left, -1):
            res[cur] = matrix[bottom][x]
            cur += 1
        for y in range(bottom, top, -1):
            res[cur] = matrix[y][left]
            cur += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    
    if left == right and top == bottom:
        res[cur] = matrix[top][left]
        return res
    
    if left == right:
        for y in range(top, bottom + 1):
            res[cur] = matrix[y][left]
            cur += 1
    
    if top == bottom:
        for x in range(left, right + 1):
            res[cur] = matrix[top][x]
            cur += 1
    return res

