#!/usr/bin/python3

def exist(board, word):
    used = [None] * len(board)
    for row in range(0, len(board)):
        used[row] = [False] * len(board[0])

    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == word[0]:
                used[row][col] = True
                if existRecursive(board, word, used, row, col, 1):
                    return True
                used[row][col] = False
    return False
                
    
def existRecursive(board, word, used, row, col, index):
    if index == len(word):
        return True

    candidates = ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
    for (i, j) in candidates:
        if 0 <= i and i < len(board) and 0 <= j and j < len(board[0]) and board[i][j] == word[index] and not used[i][j]:
            used[i][j] = True
            if existRecursive(board, word, used, i, j, index + 1):
                return True
            used[i][j] = False
    return False

print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'))
print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'))
print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'))

