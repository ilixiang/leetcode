#!/usr/bin/python3

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    i, j = m - 1, 0
    while i >= 0 and j < n:
        num = matrix[i][j]
        if num < target:
            j += 1
        elif num > target:
            i -= 1
        else:
            return True
    return False
