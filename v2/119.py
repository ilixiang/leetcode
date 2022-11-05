#!/usr/bin/python3

def getRow(rowIndex):
    rev = [1] * (rowIndex + 1)
    for i in range(0, rowIndex + 1):
        for j in range(1, i):
            rev[i - j] = rev[i - j] + rev[i - j - 1]
    return rev
