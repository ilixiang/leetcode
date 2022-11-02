#!/usr/bin/python3

def isPalindrome(x):
    if x < 0:
        return False

    quotient = x
    remainders = []
    while quotient != 0:
        remainders.append(quotient % 10)
        quotient = quotient // 10

    left = 0
    right = len(remainders) - 1
    while left <= right:
        if remainders[left] != remainders[right]:
            return False
        left = left + 1
        right = right - 1
    return True

def isPalindrome2(x):
    if x < 0:
        return False

    s = str(x)
    if s == s[::-1]:
        return True
    return False

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(0))

