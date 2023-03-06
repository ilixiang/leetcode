#!/usr/bin/python3

def setZeros(matrix):
    m, n = len(matrix), len(matrix[0])

    firstRowZero = False
    firstColZero = False
    for r in range(m):
        if matrix[r][0] == 0:
            firstColZero = True
            break
    for c in range(n):
        if matrix[0][c] == 0:
            firstRowZero = True
            break
    
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    for r in range(1, m):
        if matrix[r][0] == 0:
            for c in range(1, n):
                matrix[r][c] = 0
    for c in range(1, n):
        if matrix[0][c] == 0:
            for r in range(1, m):
                matrix[r][c] = 0
    if firstRowZero:
        for c in range(n):
            matrix[0][c] = 0
    if firstColZero:
        for r in range(m):
            matrix[r][0] = 0
