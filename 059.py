#!/usr/bin/python3

def generateMatrix(n):
    left = 0
    top = 0
    right = n - 1
    bottom = n - 1

    result = []
    for x in range(0, n):
        result.append([])
        for y in range(0, n):
            result[x].append(0)
            
    currentNum = 1
    while left < right and top < bottom:
        for y in range(left, right):
            result[top][y] = currentNum
            currentNum = currentNum + 1
        for x in range(top, bottom):
            result[x][right] = currentNum
            currentNum = currentNum + 1
        for y in range(right, left, -1):
            result[bottom][y] = currentNum
            currentNum = currentNum + 1
        for x in range(bottom, top, -1):
            result[x][left] = currentNum
            currentNum = currentNum + 1
        top = top + 1
        bottom = bottom - 1
        left = left + 1
        right = right - 1
    if left == right and top == bottom:
        result[top][left] = currentNum
    return result


