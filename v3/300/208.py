#!/usr/bin/python3

class Trie:
    def __init__(self):
        self.end = False
        self.prefixNum = 0
        self.letters = [None] * 26

    def insert(self, word):
        if len(word) == 0:
            self.end = True
            self.prefixNum += 1
            return
        letterIndex = ord(word[0]) - 97
        nextNode = self.letters[letterIndex]
        if not nextNode:
            nextNode = self.letters[letterIndex] = Trie()
        self.prefixNum += 1
        nextNode.insert(word[1:])

    def search(self, word):
        if len(word) == 0:
            return self.end
        letterIndex = ord(word[0]) - 97
        nextNode = self.letters[letterIndex]
        return  nextNode and nextNode.search(word[1:])

    def startsWith(self, prefix):
        if len(prefix) == 0:
            return self.prefixNum != 0
        letterIndex = ord(prefix[0]) - 97
        nextNode = self.letters[letterIndex]
        return nextNode and nextNode.startsWith(prefix[1:])