#!/usr/bin/python3

class WordDictionary:

    def __init__(self):
        self.letters = [None] * 26
        self.hasWord = False
        self.maxLen = 0
        self.minLen = 27

    def addWord(self, word: str) -> None:
        self.minLen = min(self.minLen, len(word))
        self.maxLen = max(self.maxLen, len(word))

        if '' == word:
            self.hasWord = True
            return
        letter = ord(word[0]) - 97
        nextLevel = self.letters[letter]
        if nextLevel == None:
            self.letters[letter] = nextLevel = WordDictionary()
        nextLevel.addWord(word[1:])
        
    def search(self, word: str) -> bool:
        if len(word) < self.minLen or len(word) > self.maxLen:
            return False
        if '' == word:
            return self.hasWord

        if '.' != word[0]:
            letter = ord(word[0]) - 97
            return None != self.letters[letter] and self.letters[letter].search(word[1:])
        for c in self.letters:
            if c != None and c.search(word[1:]):
                return True
        return False
