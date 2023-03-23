#!/usr/bin/python3

def generate(rowIndex):
    numRows = rowIndex + 1
    rev = [1] * numRows
    for row in range(numRows):
        for col in range(row - 1, 0, -1):
            rev[col] = rev[col] + rev[col - 1]
    return rev
