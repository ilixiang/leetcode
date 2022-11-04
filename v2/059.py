#!/usr/bin/python3

def generateMatrix(n):
    matrix = [None] * n
    for row in range(0, n):
        matrix[row] = [None] * n
    
    val = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1
    while left < right and top < bottom:
        for x in range(left, right):
            matrix[top][x] = val
            val += 1
        for y in range(top, bottom):
            matrix[y][right] = val
            val += 1
        for x in range(right, left, -1):
            matrix[bottom][x] = val
            val += 1
        for y in range(bottom, top, -1):
            matrix[y][left] = val
            val += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    
    if left == right and top == bottom:
        matrix[top][left] = val
        return matrix
    
    if left == right:
        for y in range(top, bottom):
            matrix[y][left] = val
            val += 1
        
    if top == bottom:
        for x in range(left, right):
            matrix[top][x] = val
            val += 1
    return matrix
