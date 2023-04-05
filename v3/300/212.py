#!/usr/bin/python3

def findWords(board, words):
    m = len(board)
    n = len(board[0])
    END_INDEX = 26
    NON_NONE_NUM_INDEX = 27

    root = [None] * 28
    root[NON_NONE_NUM_INDEX] = 0
    for word in words:
        node = root
        for letter in word:
            index = ord(letter) - 97
            if not node[index]:
                node[index] = [None] * 28
                node[index][NON_NONE_NUM_INDEX] = 0
                node[NON_NONE_NUM_INDEX] += 1
            node = node[index]
        node[END_INDEX] = word
        node[NON_NONE_NUM_INDEX] += 1

    used = [[False for j in range(n)] for i in range(m)]
    rev = []
    def dfs(row, col, trieNode):
        if used[row][col]:
            return
        
        index = ord(board[row][col]) - 97
        nextNode = trieNode[index]
        if not nextNode:
            return
        
        matchedWord = nextNode[END_INDEX]
        if matchedWord:
            rev.append(matchedWord)
            nextNode[END_INDEX] = None
            nextNode[NON_NONE_NUM_INDEX] -= 1

        used[row][col] = True
        if row - 1 >= 0:
            dfs(row - 1, col, nextNode)
        if row + 1 < m:
            dfs(row + 1, col, nextNode)
        if col - 1 >= 0:
            dfs(row, col - 1, nextNode)
        if col + 1 < n:
            dfs(row, col + 1, nextNode)
        used[row][col] = False
        if not nextNode[NON_NONE_NUM_INDEX]:
            trieNode[index] = None
            trieNode[NON_NONE_NUM_INDEX] -= 1

    for row in range(m):
        for col in range(n):
            dfs(row, col, root)
    return rev
