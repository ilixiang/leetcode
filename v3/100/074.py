#!/usr/bin/python3

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    s = m * n
    left, right = 0, s - 1
    while left <= right:
        mid = (left + right) >> 1
        num = matrix[mid // n][mid % n]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
