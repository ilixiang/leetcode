#!/usr/bin/python3

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]
    result = [1] * (rowIndex + 1)
    for row in range(2, rowIndex + 1):
        col = row - 1
        while col > 0:
            result[col] = result[col - 1] + result[col]
            col = col - 1
    return result

print(getRow(3))

