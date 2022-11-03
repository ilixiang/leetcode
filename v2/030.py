#!/usr/bin/python3

def findSubstring(s, words):
    wordLength = len(words[0])

    wordMap = {}
    for word in words:
        if not word in wordMap:
            wordMap[word] = 1
        else:
            wordMap[word] += 1
    
    res = []
    for start in range(0, wordLength):
        i = start
        while i + wordLength <= len(s):
            sWord = s[i: i + wordLength]
            if sWord in wordMap:
                wordMap[sWord] -= 1
                i += wordLength
                while wordMap[sWord] < 0:
                    wordMap[s[start: start + wordLength]] += 1
                    start += wordLength
                if wordMap[sWord] == 0 and i - start == wordLength * len(words):
                    res.append(start)
            else:
                while start != i:
                    wordMap[s[start: start + wordLength]] += 1
                    start += wordLength
                i += wordLength
        while start != i:
            wordMap[s[start: start + wordLength]] += 1
            start += wordLength
    return res
