#!/usr/bin/python3

def wordBreak(s, words):
    wordSet = set()
    wordLenSet = set()
    for word in words:
        wordSet.add(word)
        wordLenSet.add(len(word))

    dp = [None] * (len(s) + 1)
    dp[len(s)] = True

    return wordBreakDp(s, 0, wordSet, wordLenSet, dp)

def wordBreakDp(s, startIndex, wordSet, wordLenSet, dp):
    if dp[startIndex] != None:
        return dp[startIndex]

    for wordLen in wordLenSet:
        endIndex = startIndex + wordLen
        if endIndex <= len(s):
            word = s[startIndex:endIndex]
            if word in wordSet and wordBreakDp(s, endIndex, wordSet, wordLenSet, dp):
                dp[startIndex] = True
                return True
    dp[startIndex] = False
    return False

print(wordBreak('leetcode', ['leet', 'code']))
print(wordBreak('applepenapple', ['apple', 'pen']))
print(wordBreak('catsandog', ['cats', 'dog', 'and', 'cat']))

