#!/usr/bin/python3

def ladderLength(beginWord, endWord, wordList):
    wordLength = len(beginWord)


    wordMap = {}
    graph = [None] * len(wordList)
    for i in range(0, len(wordList)):
        wordMap[wordList[i]] = i
        graph[i] = []

    if not endWord in wordMap:
        return 0
    targetIndex = wordMap[endWord]

    for i in range(0, len(wordList)):
        word = wordList[i]
        for j in range(0, wordLength):
            for c in range(0, 26):
                if chr(97 + c) != word[j]:
                    replacedWord = word[:j] + chr(97 + c) + word[j+1:]
                    if replacedWord in wordMap:
                        nextIndex = wordMap[replacedWord]
                        graph[i].append(nextIndex)

    queue = []
    visited = [False] * len(wordList)
    for i in range(0, len(wordList)):
        diffLetters = 0
        for j in range(0, wordLength):
            if wordList[i][j] != beginWord[j]:
                diffLetters = diffLetters + 1
        if diffLetters == 1:
            visited[i] = True
            queue.append(i)

    print(graph)
    steps = 1
    while len(queue) != 0:
        queueLength = len(queue)
        for i in range(0, queueLength):
            index = queue.pop(0)
            if index == targetIndex:
                return steps + 1
            for nextIndex in graph[index]:
                if not visited[nextIndex]:
                    visited[nextIndex] = True
                    queue.append(nextIndex)
        steps = steps + 1
    return 0

print(ladderLength('hit', 'cog', ['hot','dot','dog','lot','log','cog']))

