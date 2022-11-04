#!/usr/bin/python3

def setZeroes(matrix):
    rowNum = len(matrix)
    colNum = len(matrix[0])

    firstRowZero = False
    firstColZero = False
    for i in range(0, rowNum):
        if matrix[i][0] == 0:
            firstColZero = True
            break
    for i in range(0, colNum):
        if matrix[0][i] == 0:
            firstRowZero = True
            break
    
    for row in range(1, rowNum):
        for col in range(1, colNum):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0
    
    for col in range(1, colNum):
        if matrix[0][col] == 0:
            for row in range(0, rowNum):
                matrix[row][col] = 0
        else:
            if firstRowZero:
                matrix[0][col] = 0
    for row in range(1, rowNum):
        if matrix[row][0] == 0:
            for col in range(0, colNum):
                matrix[row][col] = 0
        else:
            if firstColZero:
                matrix[row][0] = 0
    
    if firstColZero or firstRowZero:
        matrix[0][0] = 0
    