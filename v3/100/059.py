#!/usr/bin/python3

def generaterev(n):
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    i = 1
    rev = [[0 for j in range(n)] for i in range(n)]
    while left < right and top < bottom:
        for col in range(left, right):
            rev[top][col] = i
            i += 1
        for row in range(top, bottom):
            rev[row][right] = i
            i += 1
        for col in range(right, left, -1):
            rev[bottom][col] = i
            i += 1
        for row in range(bottom, top, -1):
            rev[row][left] = i
            i += 1
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    if left == right:
        rev[top][left] = i

    return rev
