#!/usr/bin/python3

def rotate(matrix):
    size = len(matrix)

    for r in range(size - 1):
        for c in range(size - 1 - r):
            matrix[r][c], matrix[size - 1 - c][size - 1 - r] = matrix[size - 1 - c][size - 1 - r], matrix[r][c]
    
    l, h = 0, size - 1
    while l < h:
        for c in range(size):
            matrix[l][c], matrix[h][c] = matrix[h][c], matrix[l][c]
        l += 1
        h -= 1
