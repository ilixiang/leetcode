#!/usr/bin/python3

def generate(numRows):
    result = [None] * numRows
    for i in range(0, numRows):
        result[i] = [1] * (i + 1)

    if numRows <= 2:
        return result
    for row in range(2, numRows):
        for col in range(1, row):
            result[row][col] = result[row - 1][col - 1] + result[row - 1][col]
    return result

print(generate(4))

