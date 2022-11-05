#!/usr/bin/python3

def ladderLength(beginWord, endWord, wordList):
    m = len(wordList)
    n = len(beginWord)

    endIndex = 0
    while endIndex < m and wordList[endIndex] != endWord:
        endIndex += 1
    if endIndex == m:
        return 0

    wildcardWordMap = {}
    for i in range(0, m):
        word = wordList[i]
        for j in range(0, n):
            wildcardWord = word[:j] + '*' + word[j+1:]
            if not wildcardWord in wildcardWordMap:
                wildcardWordMap[wildcardWord] = [word]
            else:
                wildcardWordMap[wildcardWord].append(word)
    
    rev = 1
    visited = set([beginWord])
    queue = [beginWord]
    while len(queue) != 0:
        size = len(queue)
        while size != 0:
            word = queue.pop(0)
            if word == endWord:
                return rev
            size -= 1
            for i in range(0, n):
                wildcardWord = word[:i] + '*' + word[i+1:]
                nextWordList = wildcardWordMap.get(wildcardWord, [])
                for nextWord in nextWordList:
                    if not nextWord in visited:
                        visited.add(nextWord)
                        queue.append(nextWord)
        rev += 1
    return 0
