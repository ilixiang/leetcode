#!/usr/bin/python3

class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        prefixMatrix = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m):
            s = 0
            for j in range(n):
                s += matrix[i][j]
                prefixMatrix[i + 1][j + 1] = s + prefixMatrix[i][j + 1]
        self.prefixMatrix = prefixMatrix

    def sumRegion(self, row1, col1, row2, col2):
        if row1 > row2 or col1 > col2:
            return 0
        leftUp = self.prefixMatrix[row1][col1]
        leftDown = self.prefixMatrix[row2 + 1][col1]
        rightUp = self.prefixMatrix[row1][col2 + 1]
        rightDown = self.prefixMatrix[row2 + 1][col2 + 1]
        return rightDown - leftDown - rightUp + leftUp
