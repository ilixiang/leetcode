#!/usr/bin/python3

def numIslands(grid):
    m = len(grid)
    n = len(grid[0])

    rev = 0
    for row in range(0, m):
        for col in range(0, n):
            if grid[row][col] != '1':
                continue
            grid[row][col] = '2'
            queue = [(row, col)]
            while len(queue) != 0:
                (i, j) = queue.pop(0)
                for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == '1':
                        grid[x][y] = '2'
                        queue.append((x, y))
            rev += 1
    return rev
