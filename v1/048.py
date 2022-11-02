#!/usr/bin/python3

def rotate(matrix):
    if len(matrix) == 1:
        return

    top = 0
    bottom = len(matrix) - 1
    while top < bottom:
        for col in range(0, len(matrix)):
            tmp = matrix[top][col]
            matrix[top][col] = matrix[bottom][col]
            matrix[bottom][col] = tmp
        top = top + 1
        bottom = bottom - 1

    for row in range(1, len(matrix)):
        for col in range(0, row):
            tmp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = tmp

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)

