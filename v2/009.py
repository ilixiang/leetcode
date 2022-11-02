#!/usr/bin/python3

def isPalindrome(x):
    if x < 0:
        return False

    tmp = []
    while x != 0:
        tmp.append(x % 10)
        x = x // 10

    left = 0
    right = len(tmp) - 1
    while left < right and tmp[left] == tmp[right]:
        left += 1
        right -= 1
    return left >= right
