#!/usr/bin/python3

def isPalindrome(x):
    if x < 0:
        return False
    
    tmp = []
    while x != 0:
        tmp.append(x % 10)
        x //= 10
    
    l, r = 0, len(tmp) - 1
    while l < r and tmp[l] == tmp[r]:
        l += 1
        r -= 1
    return l >= r

