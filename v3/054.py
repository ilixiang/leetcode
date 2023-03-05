#!/usr/bin/python3

def spiralOrder(matrix):
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    i = 0
    rev = [0 for i in range(len(matrix) * len(matrix[0]))]
    while left < right and top < bottom:
        for col in range(left, right):
            rev[i] = matrix[top][col]
            i += 1
        for row in range(top, bottom):
            rev[i] = matrix[row][right]
            i += 1
        for col in range(right, left, -1):
            rev[i] = matrix[bottom][col]
            i += 1
        for row in range(bottom, top, -1):
            rev[i] = matrix[row][left]
            i += 1
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    if left == right:
        for row in range(top, bottom + 1):
            rev[i] = matrix[row][left]
            i += 1
        return rev

    if top == bottom:
        for col in range(left, right + 1):
            rev[i] = matrix[top][col]
            i += 1
        return rev
        
    return rev
