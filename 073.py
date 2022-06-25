#!/usr/bin/python3

def setZeros(matrix):
    rows = set()
    cols = set()
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in rows:
        for col in range(0, len(matrix[0])):
            matrix[row][col] = 0
    for row in range(0, len(matrix)):
        for col in cols:
            matrix[row][col] = 0

def setZerosEfficient(matrix):
    clearFirstRow = False
    clearFirstCol = False
    for row in range(0, len(matrix)):   
        if matrix[row][0] == 0:
            clearFirstCol = True
            break
    for col in range(0, len(matrix[0])):
        if matrix[0][col] == 0:
            clearFirstRow = True
            break

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            for col in range(0, len(matrix[0])):
                matrix[row][col] = 0
    for col in range(1, len(matrix[0])):
        if matrix[0][col] == 0:
            for row in range(0, len(matrix)):
                matrix[row][col] = 0

    if clearFirstRow:
        for col in range(0, len(matrix[0])):
            matrix[0][col] = 0
    if clearFirstCol:
        for row in range(0, len(matrix)):
            matrix[row][0] = 0

