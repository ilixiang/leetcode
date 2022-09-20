#!/usr/bin/python3

def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    rev = 0
    for row in range(0, rows):
        for col in range(0, cols):
            index = row * cols + col
            if grid[row][col] == '0':
                visited.add(index)
            else:
                if index in visited:
                    continue
                else:
                    rev += 1
                    queue = [(row, col)]
                    visited.add(row * cols + col)
                    while len(queue) != 0:
                        (i, j) = queue.pop(0)
                        if i - 1 >= 0 and grid[i - 1][j] == '1' and not ((i - 1) * cols + j) in visited:
                            queue.append((i - 1, j))
                            visited.add((i - 1) * cols + j)
                        if i + 1 < rows and grid[i + 1][j] == '1' and not ((i + 1) * cols + j) in visited:
                            queue.append((i + 1, j))
                            visited.add((i + 1) * cols + j)
                        if j - 1 >= 0 and grid[i][j - 1] == '1' and not (i * cols + j - 1) in visited:
                            queue.append((i, j - 1))
                            visited.add(i * cols + j - 1)
                        if j + 1 < cols and grid[i][j + 1] == '1' and not (i * cols + j + 1) in visited:
                            queue.append((i, j + 1))
                            visited.add(i * cols + j + 1)
    return rev

print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

