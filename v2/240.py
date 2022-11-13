#!/usr/bin/python3

def searchMatrix(matrix, target):
    maxRow = len(matrix)
    maxCol = len(matrix[0])

    row = maxRow - 1
    col = 0
    while row >= 0 and col < maxCol:
        val = matrix[row][col]
        if val == target:
            return True
        elif val < target:
            col += 1
        else:
            row -= 1
    return False

