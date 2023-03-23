#!/usr/bin/python3

def minimumTotal(triangle):
    m = len(triangle)
    mem = [[None for j in range(m)] for i in range(m)]
    mem[m - 1] = triangle[m - 1]
    def dp(row, col):
        if mem[row][col] != None:
            return mem[row][col]
        
        mem[row][col] = triangle[row][col] + min(dp(row + 1, col), dp(row + 1, col + 1))
        return mem[row][col]
    return dp(0, 0)
        
