#!/usr/bin/python3

def rotate(matrix):
    size = len(matrix)
    if size == 1:
        return matrix

    left, right = 0, size - 1
    while left < right:
        for row in range(0, size):
            matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
        left += 1
        right -= 1
    print(matrix)

    for row in range(0, size - 1):
        for col in range(0, size - 1 - row):
            matrix[row][col], matrix[size - 1 - col][size - 1 - row] = matrix[size - 1 - col][size - 1 - row], matrix[row][col]
