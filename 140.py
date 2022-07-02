#!/usr/bin/python3

def wordBreak(s, words):
    wordLenSet = set()
    wordSet = set()
    for word in words:
        wordLenSet.add(len(word))
        wordSet.add(word)
    dp = [None] * (len(s) + 1)
    return wordBreakDp(s, 0, wordSet,wordLenSet, dp)

def wordBreakDp(s, startIndex, wordSet, wordLenSet, dp):
    if dp[startIndex] != None:
        return dp[startIndex]

    result = []
    for wordLen in wordLenSet:
        if startIndex + wordLen == len(s):
            word = s[startIndex: startIndex + wordLen]
            if word in wordSet:
                result.append(word)
        elif startIndex + wordLen < len(s):
            word = s[startIndex: startIndex + wordLen]
            if word in wordSet:
                nextResult = wordBreakDp(s, startIndex + wordLen, wordSet, wordLenSet, dp)
                for nextStr in nextResult:
                    result.append(word + ' ' + nextStr)
    dp[startIndex] = result
    return result

print(wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']))
print(wordBreak('pineapplepenapple', ['apple','pen','applepen','pine','pineapple']))

