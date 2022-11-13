#!/usr/bin/python3

def longestIncreasingPath(matrix):
    maxRow = len(matrix)
    maxCol = len(matrix[0])
    visited = [[False for col in range(0, maxCol)] for row in range(0, maxRow)]
    longestPaths = [[None for col in range(0, maxCol)] for row in range(0, maxRow)]

    def dfs(row, col):
        if longestPaths[row][col] != None:
            return longestPaths[row][col]

        options = ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
        rev = 1
        for (nextRow, nextCol) in options:
            if nextRow < maxRow and nextRow >= 0\
                and nextCol < maxCol and nextCol >= 0\
                and matrix[nextRow][nextCol] > matrix[row][col]\
                and not visited[nextRow][nextCol]:
                visited[nextRow][nextCol] = True
                rev = max(rev, 1 + dfs(nextRow, nextCol))
                visited[nextRow][nextCol] = False
        longestPaths[row][col] = rev
        return rev


    rev = 1
    for row in range(0, maxRow):
        for col in range(0, maxCol):
            rev = max(rev, dfs(row, col))
    return rev

if __name__ == '__main__':
    assert longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
