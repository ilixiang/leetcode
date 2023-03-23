#!/usr/bin/python3

def isValidSudoku(board):
    for row in range(9):
        validity = 0
        for col in range(9):
            c = board[row][col]
            if c != '.':
                num = int(c)
                if validity & (1 << num) != 0:
                    return False
                validity |= 1 << num
    
    for col in range(9):
        validity = 0
        for row in range(9):
            c = board[row][col]
            if c != '.':
                num = int(c)
                if validity & (1 << num) != 0:
                    return False
                validity |= 1 << num
    
    for box in range(9):
        validity = 0
        for pos in range(9):
            row = (box // 3) * 3 + pos // 3
            col = (box % 3) * 3 + pos % 3
            c = board[row][col]
            if c != '.':
                num = int(c)
                if validity & (1 << num) != 0:
                    return False
                validity |= 1 << num
    return True


