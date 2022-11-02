#!/usr/bin/python3

def solveSudoku(board):
    rowOptions = initRowOptions(board)
    colOptions = initColOptions(board)
    boxOptions = initBoxOptions(board)

    solveCell(board, 0, rowOptions, colOptions, boxOptions)

def solveCell(board, index, rowOptions, colOptions, boxOptions):
    if index == 81:
        return True

    row = index // 9
    col = index % 9
    if board[row][col] != '.':
        return solveCell(board, index + 1, rowOptions, colOptions, boxOptions)

    box = (row // 3) * 3 + col // 3
    options = rowOptions[row].intersection(colOptions[col]).intersection(boxOptions[box])
    if len(options) == 0:
        return False
    for num in options:
        board[row][col] = str(num)
        rowOptions[row].remove(num)
        colOptions[col].remove(num)
        boxOptions[box].remove(num)
        if solveCell(board, index + 1, rowOptions, colOptions, boxOptions):
            return True
        else:
            rowOptions[row].add(num)
            colOptions[col].add(num)
            boxOptions[box].add(num)
    board[row][col] = '.'
    return False

def initRowOptions(board):
    options = []
    for row in range(0, 9):
        s = set(range(1, 10))
        for col in range(0, 9):
            cellValue = board[row][col]
            if cellValue != '.':
                s.remove(int(cellValue))
        options.append(s)
    return options

def initColOptions(board):
    options = []
    for col in range(0, 9):
        s = set(range(1, 10))
        for row in range(0, 9):
            cellValue = board[row][col]
            if cellValue != '.':
                s.remove(int(cellValue))
        options.append(s)
    return options

def initBoxOptions(board):
    options = []
    for boxIndex in range(0, 9):
        startRow = (boxIndex // 3) * 3
        startCol = (boxIndex % 3) * 3
        s = set(range(1, 10))
        for row in range(startRow, startRow + 3):
            for col in range(startCol, startCol + 3):
                cellValue = board[row][col]
                if cellValue != '.':
                    s.remove(int(cellValue))
        options.append(s)
    return options

board = \
[["5","3",".",".","7",".",".",".","."], \
["6",".",".","1","9","5",".",".","."], \
[".","9","8",".",".",".",".","6","."], \
["8",".",".",".","6",".",".",".","3"], \
["4",".",".","8",".","3",".",".","1"], \
["7",".",".",".","2",".",".",".","6"], \
[".","6",".",".",".",".","2","8","."], \
[".",".",".","4","1","9",".",".","5"], \
[".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)
print(board)

