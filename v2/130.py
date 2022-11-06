#!/usr/bin/python3

def sovle(board):
    m = len(board)
    n = len(board[0])
    
    queue = []
    for i in range(0, m):
        if board[i][0] == 'O':
            board[i][0] = 'Y'
            queue.append((i, 0))
        if board[i][n - 1] == 'O':
            board[i][n - 1] = 'Y'
            queue.append((i, n - 1))
    for i in range(1, n - 1):
        if board[0][i] == 'O':
            board[0][i] = 'Y'
            queue.append((0, i))
        if board[m - 1][i] == 'O':
            board[m - 1][i] = 'Y'
            queue.append((m - 1, i))
    
    while len(queue) != 0:
        (i, j) = queue.pop(0)
        if i - 1 >= 0 and board[i - 1][j] == 'O':
            board[i - 1][j] = 'Y'
            queue.append((i - 1, j))
        if i + 1 < m and board[i + 1][j] == 'O':
            board[i + 1][j] = 'Y'
            queue.append((i + 1, j))
        if j - 1 >= 0 and board[i][j - 1] == 'O':
            board[i][j - 1] = 'Y'
            queue.append((i, j - 1))
        if j + 1 < n and board[i][j + 1] == 'O':
            board[i][j + 1] = 'Y'
            queue.append((i, j + 1))
    
    for i in range(0, m):
        for j in range(0, n):
            if board[i][j] == 'Y':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'

