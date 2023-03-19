#!/usr/bin/python3

def solve(board):
    m = len(board)
    n = len(board[0])

    queue = []
    def bfs(row, col):
        symbol = board[row][col]
        if symbol != 'O':
            return
        board[row][col] = 'V'
        queue.append((row, col))
        while len(queue) != 0:
            (i, j) = queue.pop(0)
            if i > 0 and board[i - 1][j] == 'O':
                board[i - 1][j] = 'V'
                queue.append((i - 1, j))
            if j > 0 and board[i][j - 1] == 'O':
                board[i][j - 1] = 'V'
                queue.append((i, j - 1))
            if i < m - 1 and board[i + 1][j] == 'O':
                board[i + 1][j] = 'V'
                queue.append((i + 1, j))
            if j < n - 1 and board[i][j + 1] == 'O':
                board[i][j + 1] = 'V'
                queue.append((i, j + 1))

    for row in range(m):
        bfs(row, 0)
        bfs(row, n - 1)
    for col in range(n):
        bfs(0, col)
        bfs(m - 1, col)
    
    for row in range(m):
        for col in range(n):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            elif board[row][col] == 'V':
                board[row][col] = 'O'
