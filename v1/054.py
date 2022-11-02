#!/usr/bin/python3

def spiralOrder(matrix):
    if len(matrix) == 0:
        return []

    result = []

    left = 0
    top = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1
    while left < right and top < bottom:
        for y in range(left, right):
            result.append(matrix[top][y])
        for x in range(top, bottom):
            result.append(matrix[x][right])
        for y in range(right, left, -1):
            result.append(matrix[bottom][y])
        for x in range(bottom, top, -1):
            result.append(matrix[x][left])
        left = left + 1
        right = right - 1
        top = top + 1
        bottom = bottom - 1

    if top == bottom:
        for y in range(left, right + 1):
            result.append(matrix[top][y])
        return result

    if left == right:
        for x in range(top, bottom + 1):
            result.append(matrix[x][left])
    return result

print(spiralOrder([[1]]))
print(spiralOrder([[1, 2, 3]]))
print(spiralOrder([[1], [2], [3]]))
print(spiralOrder([[1, 2, 3], [4, 5, 6]]))
print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

            
            


