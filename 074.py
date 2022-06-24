#!/usr/bin/python3

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    low = 0
    high = m * n
    mid = (low + high) // 2

    while low < high:
        mIndex = mid // n
        nIndex = mid % n
        val = matrix[mIndex][nIndex]
        if target == val:
            return True
        elif target < val:
            high = mid
        else:
            low = mid + 1
        mid = (low + high) // 2
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))

