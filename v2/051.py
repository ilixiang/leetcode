#!/usr/bin/python3

def solveNQueens(n):
    usedCols = [0] * n
    board = [None] * n
    for row in range(0, len(board)):
        board[row] = ['.'] * n
    
    res = []
    solveNQueensRecursive(n, board, 0, usedCols, res)
    return res
    
def solveNQueensRecursive(n, board, curRow, usedCols, res):
    if n == curRow:
        res.append(list(map(lambda r: ''.join(r), board)))
        return

    used = 0
    for i in range(0, curRow):
        usedCol = usedCols[i]
        used |= usedCol
        used |= usedCol << (curRow - i)
        used |= usedCol >> (curRow - i)
    
    for col in range(0, n):
        if used & (1 << col) != 0:
            continue
        board[curRow][col] = 'Q'
        usedCols[curRow] |= 1 << col
        solveNQueensRecursive(n, board, curRow + 1, usedCols, res)
        board[curRow][col] = '.'
        usedCols[curRow] &= ~(1 << col)
