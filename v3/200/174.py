#!/usr/bin/python3

def calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    cache = [[None for j in range(n)] for i in range(m)]
    cache[m - 1][n - 1] = 0 if dungeon[m - 1][n - 1] >= 0 else -dungeon[m - 1][n - 1]

    def dp(i, j):
        if cache[i][j] != None:
            return cache[i][j]
        
        right = down = None
        if i < m - 1:
            down = dp(i + 1, j) - dungeon[i][j]
            if down < 0:
                down = 0
        if j < n - 1:
            right = dp(i, j + 1) - dungeon[i][j]
            if right < 0:
                right = 0
        cache[i][j] = min(filter(lambda x: x != None, [right, down]))
        return cache[i][j]
    return 1 + dp(0, 0)
