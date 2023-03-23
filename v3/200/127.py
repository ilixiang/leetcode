#!/usr/bin/python3

def ladderLength(beginWord, endWord, wordList):
    wordLength = len(wordList[0])
    wildcardWordMap = {}
    for word in wordList:
        for i in range(wordLength):
            wildcardWord = word[:i] + '*' + word[i + 1:]
            wildcardWordMapping = wildcardWordMap.get(wildcardWord, None)
            if wildcardWordMapping == None:
                wildcardWordMap[wildcardWord] = [word]
            else:
                wildcardWordMapping.append(word)

    rev = 1
    used = set()
    queue = [beginWord]
    while len(queue) != 0:
        curLayerCount = len(queue)
        while curLayerCount > 0:
            curWord = queue.pop(0)
            if curWord == endWord:
                return rev
            for i in range(wordLength):
                wildcardWord = curWord[0:i] + '*' + curWord[i + 1:]
                nextWords = wildcardWordMap.get(wildcardWord, [])
                for nextWord in nextWords:
                    if not nextWord in used:
                        used.add(nextWord)
                        queue.append(nextWord)
            curLayerCount -= 1
        rev += 1
    return 0
