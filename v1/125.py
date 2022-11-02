#!/usr/bin/python3

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left = left + 1
        while left < right and not ((s[left] <= 'z' and s[left] >= 'a') or (s[left] <= 'Z' and s[left] >= 'A') or (s[left] <= '9' and s[left] >= '0')):
            left = left + 1
        right = right - 1
        while left < right and not ((s[right] <= 'z' and s[right] >= 'a') or (s[right] <= 'Z' and s[right] >= 'A') or (s[right] <= '9' and s[right] >= '0')):
            right = right - 1
        print(left, right)
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
print(isPalindrome('0P'))

