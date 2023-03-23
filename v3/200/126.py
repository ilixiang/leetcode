#!/usr/bin/python3

class ListNode:
    def __init__(self, val, prev = None):
        self.val = val
        self.prevSet = set()
        if prev:
            self.prevSet.add(prev)
    
    def addPrev(self, prev):
        if prev:
            self.prevSet.add(prev)
    
    def getPrevs(self):
        return self.prevSet

def findLadders(beginWord, endWord, wordList):
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

    used = set()
    queue = [ListNode(beginWord)]
    endWordNode = None
    while len(queue) != 0:
        if endWordNode:
            break

        curLayerCount = len(queue)
        curLayerNodeCache = {}
        while curLayerCount > 0:
            curWordNode = queue.pop(0)
            curWord = curWordNode.val
            for i in range(wordLength):
                wildcardWord = curWord[0:i] + '*' + curWord[i + 1:]
                nextWords = wildcardWordMap.get(wildcardWord, [])
                for nextWord in nextWords:
                    if not nextWord in used:
                        nextWordNode = curLayerNodeCache.get(nextWord, None)
                        if not nextWordNode:
                            curLayerNodeCache[nextWord] = nextWordNode = ListNode(nextWord, curWordNode)
                            queue.append(nextWordNode)
                        else:
                            nextWordNode.addPrev(curWordNode)

                        if nextWord == endWord:
                            endWordNode = nextWordNode
            curLayerCount -= 1
        used.update(curLayerNodeCache.keys())
    
    if not endWordNode:
        return []

    rev = []
    tmp = []
    def dfs(node):
        tmp.append(node.val)
        prevNodes = node.getPrevs()
        if len(prevNodes) == 0:
            tmpCopy = list(tmp)
            tmpCopy.reverse()
            rev.append(tmpCopy)
            tmp.pop()
            return

        for prevNode in prevNodes:
            dfs(prevNode)
        tmp.pop()
    
    dfs(endWordNode)
    return rev
