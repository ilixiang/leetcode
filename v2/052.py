#!/usr/bin/python3

def totalNQueens(n):
    usedCols = [0] * n
    return totalNQueensRecursive(n, 0, usedCols)

def totalNQueensRecursive(n, curRow, usedCols):
    if n == curRow:
        return 1
    
    used = 0
    for row in range(0, curRow):
        usedCol = usedCols[row]
        used |= usedCol
        used |= usedCol << (curRow - row)
        used |= usedCol >> (curRow - row)
    
    res = 0
    for i in range(0, n):
        if used & (1 << i) != 0:
            continue
        usedCols[curRow] |= 1 << i
        res += totalNQueensRecursive(n, curRow + 1, usedCols)
        usedCols[curRow] &= ~(1 << i)
    return res
