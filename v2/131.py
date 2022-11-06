#!/usr/bin/python3

def partition(s):
    m = len(s)
    dp = [None] * m
    palindrome = [None] * m
    for i in range(0, m):
        dp[i] = [None] * m
        palindrome[i] = [None] * m
    
    def isPalindrom(sStart, sEnd):
        if palindrome[sStart][sEnd - 1] != None:
            return palindrome[sStart][sEnd - 1]
        
        left, right = sStart, sEnd - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        palindrome[sStart][sEnd - 1] = left >= right
        return palindrome[sStart][sEnd - 1]

    
    def partitionDp(sStart, dividers):
        if sStart == m and dividers == -1:
            return [[]]
        if sStart == m or dividers == -1:
            return []
        
        if dp[sStart][dividers] != None:
            return dp[sStart][dividers]
        
        i = sStart + 1
        rev = []
        while i <= m:
            if not isPalindrom(sStart, i):
                i += 1
                continue
            nextPartitions = partitionDp(i, dividers - 1)
            for nextPartition in nextPartitions:
                tmp = [s[sStart: i]]
                tmp.extend(nextPartition)
                rev.append(tmp)
            i += 1
        dp[sStart][dividers] = rev
        return rev
    
    rev = []
    for dividers in range(0, m):
        rev.extend(partitionDp(0, dividers))
    return rev

if __name__ == '__main__':
    print(partition('aab'))
    