#!/usr/bin/python3

def longestCommonSubsequence(text1, text2):
    l1 = len(text1)
    l2 = len(text2)

    dp = [[0 for j in range(0, l2 + 1)] for i in range(0, l1 + 1)]
    for i in range(l1 - 1, -1, -1):
        for j in range(l2 - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]

if __name__ == '__main__':
    assert longestCommonSubsequence('abcde', 'ace') == 3
    assert longestCommonSubsequence('abc', 'abc') == 3
    assert longestCommonSubsequence('abc', 'def') == 0
