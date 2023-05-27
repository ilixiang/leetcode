#!/usr/bin/python3

def gameOfLife(board):
    surroundingDiffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            tmp = board[i][j] * 10
            for (iDiff, jDiff) in surroundingDiffs:
                x, y = i + iDiff, j + jDiff
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if x < i or (x == i and y < j):
                    tmp += board[x][y] // 10
                else:
                    tmp += board[x][y]
            board[i][j] = tmp
    
    for i in range(m):
        for j in range(n):
            origin = board[i][j] // 10
            surrounding = board[i][j] % 10
            if surrounding < 2 or surrounding > 3:
                board[i][j] = 0
            elif surrounding == 3:
                board[i][j] = 1
            else:
                board[i][j] = origin

