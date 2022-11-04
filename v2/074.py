#!/usr/bin/python3

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n
    while left < right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid
    return False
