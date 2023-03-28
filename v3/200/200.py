#!/usr/bin/python3

def numIslands(grid):
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):
        grid[i][j] = '2'
        if i > 0 and grid[i - 1][j] == '1':
            dfs(i - 1, j)
        if j > 0 and grid[i][j - 1] == '1':
            dfs(i, j - 1)
        if i < m - 1 and grid[i + 1][j] == '1':
            dfs(i + 1, j)
        if j < n - 1 and grid[i][j + 1] == '1':
            dfs(i, j + 1)
    
    rev = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                rev += 1
    return rev
