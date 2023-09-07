#!/usr/bin/python3

def isPerfectSquare(self, num: int) -> bool:
    if num == 1:
        return True
    left, right = 1, num
    while left <= right:
        mid = (left + right) >> 1
        square = mid ** 2
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

