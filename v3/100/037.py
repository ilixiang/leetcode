#!/usr/bin/python3

def solveSudoku(board):
    rowValidities = [0] * 9
    colValidities = [0] * 9
    boxValidities = [0] * 9

    for row in range(9):
        for col in range(9):
            if board[row][col] != '.':
                val = int(board[row][col])
                rowValidities[row] |= (1 << val)
                colValidities[col] |= (1 << val)
                boxValidities[(row // 3) * 3 + (col // 3)] |= (1 << val)

    def solveRecursive(pos):
        if pos == 81:
            return True

        row, col = pos // 9, pos % 9
        box = (row // 3) * 3 + (col // 3)
        symbol = board[row][col]
        if symbol == '.':
            for val in range(1, 10):
                if (rowValidities[row] & (1 << val) == 0)\
                    and (colValidities[col] & (1 << val) == 0)\
                    and (boxValidities[box] & (1 << val) == 0):

                    board[row][col] = str(val)
                    rowValidities[row] |= (1 << val)
                    colValidities[col] |= (1 << val)
                    boxValidities[box] |= (1 << val)
                    if solveRecursive(pos + 1):
                        return True
                    
                    board[row][col] = '.'
                    rowValidities[row] &= ~(1 << val)
                    colValidities[col] &= ~(1 << val)
                    boxValidities[box] &= ~(1 << val)
            return False
        else:
            return solveRecursive(pos + 1)
        
    solveRecursive(0)
