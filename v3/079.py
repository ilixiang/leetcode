#!/usr/bin/python3

def exist(board, word):
    m, n = len(board), len(board[0])
    length = len(word)
    if length > m * n:
        return False
    
    wordCounter = {}
    for c in word:
        wordCounter[c] = wordCounter.get(c, 0) + 1
    boardCounter = {}
    for i in range(m):
        for j in range(n):
            c = board[i][j]
            boardCounter[c] = boardCounter.get(c, 0) + 1
    for c in wordCounter:
        if wordCounter[c] > boardCounter.get(c, 0):
            return False
    
    used = [[False for j in range(n)] for i in range(m)]
    def existRecursive(i, j, k):
        if k == length:
            return True
        
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k] or used[i][j]:
            return False
        
        used[i][j] = True
        rev = existRecursive(i - 1, j, k + 1) or existRecursive(i + 1, j, k + 1)\
            or existRecursive(i, j - 1, k + 1) or existRecursive(i, j + 1, k + 1)
        used[i][j] = False
        return rev
    
    return any(existRecursive(i, j, 0) for i in range(m) for j in range(n))
