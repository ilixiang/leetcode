#!/usr/bin/python3

def totalNQueens(n):
    rev = 0
    colUseds = [0 for i in range(n)]
    def recursive(i):
        if i == n:
            rev += 1
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
                colUseds[i] = (1 << col)
                recursive(i + 1)
                colUseds[i] = 0

    recursive(0)
    return rev