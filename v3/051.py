#!/usr/bin/python3

def solveNQueens(n):
    rev = []
    colUseds = [0 for i in range(n)]
    tmp = [['.' for j in range(n)] for i in range(n)]
    def recursive(i):
        if i == n:
            rev.append(list(map(lambda e: ''.join(e), tmp)))
            return

        slashUsed = 0
        colUsed = 0
        for row in range(i):
            prevColUsed = colUseds[row]
            colUsed |= prevColUsed
            slashUsed |= (prevColUsed << (i - row))
            slashUsed |= (prevColUsed >> (i - row))
        
        for col in range(n):
            if slashUsed & (1 << col) == 0 and colUsed & (1 << col) == 0:
                tmp[i][col] = 'Q'
                colUseds[i] = (1 << col)
                recursive(i + 1)
                tmp[i][col] = '.'
                colUseds[i] = 0

    recursive(0)
    return rev