#!/usr/bin/python3

def solveSudoku(board):
    rowValidities = [0] * 9
    colValidities = [0] * 9
    boxValidities = [0] * 9

    unfilledPositions = []

    for row in range(0, 9):
        for col in range(0, 9):
            val = board[row][col]
            if val != '.':
                val = int(val)
                rowValidities[row] |= (1 << val)
                colValidities[col] |= (1 << val)
                boxValidities[(row // 3) * 3 + (col // 3)] |= (1 << val)
            else:
                unfilledPositions.append((row, col))
    
    solveSudokuRecursive(board, rowValidities, colValidities, boxValidities, unfilledPositions, 0)

def solveSudokuRecursive(board, rowValidities, colValidities, boxValidities, unfilledPositions, curPosition):
    if curPosition == len(unfilledPositions):
        return True

    (row, col) = unfilledPositions[curPosition]
    for val in range(1, 10):
        shiftedVal = 1 << val
        if (rowValidities[row] & shiftedVal == 0)\
            and (colValidities[col] & shiftedVal == 0)\
            and (boxValidities[(row // 3) * 3 + (col // 3)] & shiftedVal == 0):
            rowValidities[row] |= shiftedVal
            colValidities[col] |= shiftedVal
            boxValidities[(row // 3) * 3 + (col // 3)] |= shiftedVal
            if solveSudokuRecursive(board, rowValidities, colValidities, boxValidities, unfilledPositions, curPosition + 1):
                board[row][col] = str(val)
                return True
            else:
                shiftedValComplement = ~shiftedVal
                rowValidities[row] &= shiftedValComplement
                colValidities[col] &= shiftedValComplement 
                boxValidities[(row // 3) * 3 + (col // 3)] &= shiftedValComplement
    return False
