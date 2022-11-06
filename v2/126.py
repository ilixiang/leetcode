#!/usr/bin/python3

def findLadders(beginWord, endWord, wordList):
    m = len(wordList)
    n = len(beginWord)

    if not endWord in wordList:
        return []
    
    wildcardWordMap = {}
    for i in range(0, m):
        word = wordList[i]
        for j in range(0, n):
            wildcardWord = word[:j] + '*' + word[j+1:]
            if not wildcardWord in wildcardWordMap:
                wildcardWordMap[wildcardWord] = [wordList[i]]
            else:
                wildcardWordMap[wildcardWord].append(wordList[i])
    
    pathLength = 1
    revPaths = []
    queue = [(beginWord, None)]
    visited = set([beginWord])
    while len(queue) != 0:
        size = len(queue)
        curLevelVisitedMap = {}
        while size != 0:
            wordTuple = queue.pop(0)
            (word, sources) = wordTuple
            size -= 1
            if word == endWord:
                revPaths.append(wordTuple)
            for i in range(0, n):
                wildcardWord = word[:i] + '*' + word[i+1:]
                for nextWord in wildcardWordMap.get(wildcardWord, []):
                    if not nextWord in visited:
                        if not nextWord in curLevelVisitedMap:
                            nextWordTuple = (nextWord, [wordTuple])
                            queue.append(nextWordTuple)
                            curLevelVisitedMap[nextWord] = nextWordTuple
                        else:
                            curLevelVisitedMap[nextWord][1].append(wordTuple)

        if len(revPaths) != 0:
            print(revPaths)
            rev = []
            for revPath in revPaths:
                tmp = [None] * pathLength
                def traverse(t, i):
                    tmp[i] = t[0]
                    if i == 0:
                        rev.append(list(tmp))
                        return
                    nexts = t[1]
                    for n in nexts:
                        traverse(n, i - 1)
                traverse(revPath, pathLength - 1)
            return rev

        visited.update(curLevelVisitedMap.keys())
        pathLength += 1
    return []

if __name__ == '__main__':
    wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = "hit"
    endWord = "cog"
    print(findLadders(beginWord, endWord, wordList))
