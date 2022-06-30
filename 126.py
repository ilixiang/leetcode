#!/usr/bin/python3

def findLadders(beginWord, endWord, wordList):
    wordLength = len(beginWord)
    targetIndex = None
    graph = {}
    for i in range(0, len(wordList)):
        if wordList[i] == endWord:
            targetIndex = i
        graph[i] = set()
    if targetIndex == None:
        return []

    for i in range(0, len(wordList)):
        for j in range(i + 1, len(wordList)):
            iWord = wordList[i]
            jWord = wordList[j]
            differentLetterCount = 0
            for k in range(0, wordLength):
                if iWord[k] != jWord[k]:
                    differentLetterCount = differentLetterCount + 1
            if differentLetterCount == 1:
                graph[i].add(j)
                graph[j].add(i)
    indexSet = set()
    for i in range(0, len(wordList)):
        word = wordList[i]
        differentLetterCount = 0
        for j in range(0, wordLength):
            if word[j] != beginWord[j]:
                differentLetterCount = differentLetterCount + 1
        if differentLetterCount == 1:
            indexSet.add(i)

    visited = set(indexSet)
    indicesResults = findPath(indexSet, targetIndex, graph, visited)
    result = []
    for indices in indicesResults:
        result.append([beginWord] + list(map(lambda index: wordList[index], indices)))
    return result

def findPath(indexSet, targetIndex, graph, visited):
    if len(indexSet) == 0:
        return []

    if targetIndex in indexSet:
        return [[targetIndex]]
    nextIndexSet = set()
    for index in indexSet:
        adjacentIndices = graph[index]
        for adjacentIndex in adjacentIndices:
            if not adjacentIndex in visited:
                nextIndexSet.add(adjacentIndex)
                visited.add(adjacentIndex)
    nextResults = findPath(nextIndexSet, targetIndex, graph, visited)
    result = []
    for nextResult in nextResults:
        nextIndex = nextResult[0]
        for index in graph[nextIndex].intersection(indexSet):
            result.append([index] + nextResult)
    return result

print(findLadders('hit', 'cog', ['hot','dot','dog','lot','log','cog']))
print(findLadders('hit', 'cog', ['hot','dot','dog','lot','log']))
