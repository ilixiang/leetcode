#!/usr/bin/python3

def isValidSudoku(board):
    for row in range(0, 9):
        if not isValidRow(board, row):
            return False
    for col in range(0, 9):
        if not isValidCol(board, col):
            return False
    for box in range(0, 9):
        if not isValidBox(board, box):
            return False
    return True

def isValidRow(board, row):
    exists = [False] * 10
    for element in board[row]:
        if element == '.':
            continue
        num = int(element)
        if exists[num]:
            return False
        exists[num] = True
    return True

def isValidCol(board, col):
    exists = [False] * 10
    for row in range(0, 9):
        element = board[row][col]
        if element == '.':
            continue
        num = int(element)
        if exists[num]:
            return False
        exists[num] = True
    return True

def isValidBox(board, box):
    exists = [False] * 10
    startRow = (box // 3) * 3
    startCol = (box % 3) * 3
    for row in range(startRow, startRow + 3):
        for col in range(startCol, startCol + 3):
            element = board[row][col]
            if element == '.':
                continue
            
            num = int(element)
            if exists[num]:
                return False
            exists[num] = True
    return True
            
board = \
[["5","3",".",".","7",".",".",".","."] \
,["6",".",".","1","9","5",".",".","."] \
,[".","9","8",".",".",".",".","6","."] \
,["8",".",".",".","6",".",".",".","3"] \
,["4",".",".","8",".","3",".",".","1"] \
,["7",".",".",".","2",".",".",".","6"] \
,[".","6",".",".",".",".","2","8","."] \
,[".",".",".","4","1","9",".",".","5"] \
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))

board = \
[["8","3",".",".","7",".",".",".","."] \
,["6",".",".","1","9","5",".",".","."] \
,[".","9","8",".",".",".",".","6","."] \
,["8",".",".",".","6",".",".",".","3"] \
,["4",".",".","8",".","3",".",".","1"] \
,["7",".",".",".","2",".",".",".","6"] \
,[".","6",".",".",".",".","2","8","."] \
,[".",".",".","4","1","9",".",".","5"] \
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
