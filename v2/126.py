#!/usr/bin/python3

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

class TreeNode:
    def __init__(self, val, child = None, sibling = None):
        self.val = val
        self.child = child
        self.sibling = sibling
    
    def appendChild(self, child):
        n = self.child
        while n != None and child.val != n.val:
            n = n.sibling
        if n != None:
            return

        if self.child == None:
            self.child = child
        else:
            self.child.appendSibling(child)
    
    def appendSibling(self, sibling):
        if self.sibling != None:
            sibling.sibling = self.sibling
        self.sibling = sibling
    
    def getSibling(self):
        return self.sibling
    
def printTreeNode(node):
    if node == None:
        return
    print('----------')
    queue = [node]
    while len(queue) != 0:
        print(list(map(lambda n: n.val, queue)))
        size = len(queue)
        while size != 0:
            cur = queue.pop(0)
            child = cur.child
            while child != None:
                queue.append(child)
                child = child.sibling
            size -= 1
    print('----------')

def findLadders(beginWord, endWord, wordList):
    m = len(wordList)
    n = len(beginWord)

    if not endWord in wordList:
        return []
    
    wordTreeNodeList = [None] * m
    for i in range(0, m):
        wordTreeNodeList[i] = TreeNode(wordList[i])
    
    wildcardWordMap = {}
    for i in range(0, m):
        word = wordList[i]
        for j in range(0, n):
            wildcardWord = word[:j] + '*' + word[j+1:]
            if not wildcardWord in wildcardWordMap:
                wildcardWordMap[wildcardWord] = [wordTreeNodeList[i]]
            else:
                wildcardWordMap[wildcardWord].append(wordTreeNodeList[i])
    
    pathLength = 1
    revDummyNode = ListNode(None)
    revLastNode = revDummyNode
    queue = [TreeNode(beginWord)]
    visited = set([beginWord])
    while len(queue) != 0:
        size = len(queue)
        curLevelVisited = set()
        while size != 0:
            wordNode = queue.pop(0)
            word = wordNode.val
            size -= 1
            if word == endWord:
                printTreeNode(wordNode)
                revLastNode.next = ListNode(wordNode)
                revLastNode = revLastNode.next
                continue
            for i in range(0, n):
                wildcardWord = word[:i] + '*' + word[i+1:]
                for nextWordTreeNode in wildcardWordMap.get(wildcardWord, []):
                    nextWord = nextWordTreeNode.val
                    if not nextWord in visited:
                        nextWordTreeNode.appendChild(wordNode)
                        if not nextWord in curLevelVisited:
                            queue.append(nextWordTreeNode)
                            curLevelVisited.add(nextWord)


        if revDummyNode.next != None:
            node = revDummyNode.next
            while node != None:
                node = node.next
            revNode = revDummyNode.next
            rev = []
            tmp = [None] * pathLength
            while revNode != None:
                treeNode = revNode.val
                def traverseTreeNode(node, seq):
                    tmp[seq] = node.val
                    if node.child == None:
                        rev.append(list(tmp))
                        return
                    child = node.child
                    while child != None:
                        traverseTreeNode(child, seq - 1)
                        child = child.sibling
                traverseTreeNode(treeNode, pathLength - 1)
                revNode = revNode.next
            return rev

        visited.update(curLevelVisited)
        pathLength += 1
    return []

if __name__ == '__main__':
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    beginWord = "red"
    endWord = "tax"
    print(findLadders(beginWord, endWord, wordList))
