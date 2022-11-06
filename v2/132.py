#!/usr/bin/python3

def minCut(s):
    m = len(s)
    dp = [None] * m
    palindrome = [None] * m
    for i in range(0, m):
        palindrome[i] = [None] * m
    
    def isPalindrom(sStart, sEnd):
        print(sStart, sEnd)
        if sStart >= sEnd:
            return True

        if palindrome[sStart][sEnd - 1] != None:
            return palindrome[sStart][sEnd - 1]

        if sStart == sEnd - 1:
            palindrome[sStart][sEnd - 1] = True
            return True
        
        palindrome[sStart][sEnd - 1] = s[sStart] == s[sEnd - 1] and isPalindrom(sStart + 1, sEnd - 1)
        return palindrome[sStart][sEnd - 1]

    def minCutDp(sStart):
        if sStart == m:
            return -1
        
        if dp[sStart] != None:
            return dp[sStart]
        
        rev = m - 1 - sStart
        i = sStart + 1
        while i <= m:
            if not isPalindrom(sStart, i):
                i += 1
                continue
            rev = min(rev, 1 + minCutDp(i))
            i += 1
        dp[sStart] = rev
        return rev 
    
    return minCutDp(0)

if __name__ == '__main__':
    print(minCut('fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi'))
