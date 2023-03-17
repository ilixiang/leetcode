#!/usr/bin/python3

def generate(numRows):
    rev = [None] * numRows
    tmp = [1] * numRows
    for row in range(numRows):
        for col in range(row - 1, 0, -1):
            tmp[col] = tmp[col] + tmp[col - 1]
        rev[row] = tmp[:row + 1]
    return rev
