#!/usr/bin/python3

def isValidSudoku(board):
    s = 0
    for row in range(0, 9):
        for col in range(0, 9):
            val = board[row][col]
            if val != '.':
                val = int(val)
                if s & (1 << val) != 0:
                    return False
                s |= (1 << val)
        s = 0

    for col in range(0, 9):
        for row in range(0, 9):
            val = board[row][col]
            if val != '.':
                val = int(val)
                if s & (1 << val) != 0:
                    return False
                s |= (1 << val)
        s = 0

    for box in range(0, 9):
        for orderNo in range(0, 9):
            row = (box // 3) * 3 + orderNo // 3
            col = (box % 3) * 3 + orderNo % 3
            val = board[row][col]
            if val != '.':
                val = int(val)
                if s & (1 << val) != 0:
                    return False
                s |= (1 << val)
        s = 0
    return True