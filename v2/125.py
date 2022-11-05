#!/usr/bin/python3

def isPalindrome(s):
    s = ''.join(map(str.lower, filter(str.isalnum, list(s))))
    left, right = 0, len(s) - 1
    while left < right and s[left] == s[right]:
        left += 1
        right -= 1
    return left >= right
