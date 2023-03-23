#!/usr/bin/python3

def minCut(s):
    if len(s) == 0:
        return 0

    palindromeCache = [[None for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        palindromeCache[i][i] = True
    def isPalindrome(i, j):
        if i > j:
            return True
        if palindromeCache[i][j] != None:
            return palindromeCache[i][j]
        palindromeCache[i][j] = s[i] == s[j] and isPalindrome(i + 1, j - 1)
        return palindromeCache[i][j]
    
    minCutCache = [None for i in range(len(s) + 1)]
    minCutCache[len(s)] = 0
    def recursive(start):
        if minCutCache[start] != None:
            return minCutCache[start]

        rev = len(s) - 1 - start
        if isPalindrome(start, len(s) - 1):
            minCutCache[start] = rev = 0
            return rev
        for end in range(start, len(s) - 1):
            if isPalindrome(start, end):
                rev = min(rev, 1 + recursive(end + 1))
        minCutCache[start] = rev
        return rev
    return recursive(0)
