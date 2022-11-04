#!/usr/bin/python3

def exist(board, word):
    m = len(board)
    n = len(board[0])
    length = len(word)
    used = [None] * m
    for i in range(0, m):
        used[i] = [False] * n
    for r in range(0, m):
        for c in range(0, n):
            used[r][c] = True
            if existRecursive(board, word, m, n, length, used, r, c, 0):
                return True
            used[r][c] = False
    return False

def existRecursive(board, word, m, n, length, used, row, col, i):
    if board[row][col] != word[i]:
        return False
    
    if i == length - 1:
        return True
    
    if row != 0 and not used[row - 1][col]:
        used[row - 1][col] = True
        if existRecursive(board, word, m, n, length, used, row - 1, col, i + 1):
            return True
        used[row - 1][col] = False
    
    if row != m - 1 and not used[row + 1][col]:
        used[row + 1][col] = True
        if existRecursive(board, word, m, n, length, used, row + 1, col, i + 1):
            return True
        used[row + 1][col] = False
    
    if col != 0 and not used[row][col - 1]:
        used[row][col - 1] = True
        if existRecursive(board, word, m, n, length, used, row, col - 1, i + 1):
            return True
        used[row][col - 1] = False
    
    if col != n - 1 and not used[row][col + 1]:
        used[row][col + 1] = True
        if existRecursive(board, word, m, n, length, used, row, col + 1, i + 1):
            return True
        used[row][col + 1] = False
    return False
