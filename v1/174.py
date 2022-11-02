#!/usr/bin/python3

def calculateMinimumHP(dungeon):
    maxRow = len(dungeon)
    maxCol = len(dungeon[0])
    dp = [None] * maxRow
    for i in range(0, maxRow):
        dp[i] = [None] * maxCol
    dp[maxRow - 1][maxCol - 1] = (1 - dungeon[maxRow - 1][maxCol - 1]) if dungeon[maxRow - 1][maxCol - 1] < 0 else 1
    result = calculateMinimumHPDp(dungeon, 0, 0, dp)
    print(dp)
    return result

def calculateMinimumHPDp(dungeon, row, col, dp):
    if dp[row][col] != None:
        return dp[row][col]

    if row == len(dungeon) - 1:
        neededHp = -1 * dungeon[row][col] + calculateMinimumHPDp(dungeon, row, col + 1, dp)
        dp[row][col] = neededHp if neededHp > 0 else 1
    elif col == len(dungeon[0]) - 1:
        neededHp = -1 * dungeon[row][col] + calculateMinimumHPDp(dungeon, row + 1, col, dp)
        dp[row][col] = neededHp if neededHp > 0 else 1
    else:
        neededHp = -1 * dungeon[row][col] + min(calculateMinimumHPDp(dungeon, row + 1, col, dp), calculateMinimumHPDp(dungeon, row, col + 1, dp))
        dp[row][col] = neededHp if neededHp > 0 else 1
    return dp[row][col]

print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(calculateMinimumHP([[0]]))

