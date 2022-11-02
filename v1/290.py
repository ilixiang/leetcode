#!/usr/bin/python3

def wordPattern(pattern, s):
    pIndex = 0
    sIndex = 0
    pLength = len(pattern)
    sLength = len(s)
    
    m = {}
    wordSet = set()

    while pIndex < pLength and sIndex < sLength:
        pChar = pattern[pIndex]
        pIndex += 1

        while sIndex < sLength and s[sIndex] == ' ':
            sIndex += 1
        sStartIndex = sIndex
        while sIndex < sLength and s[sIndex] != ' ':
            sIndex += 1
        sEndIndex = sIndex
        sWord = s[sStartIndex: sEndIndex]

        if sWord == '':
            return False

        if not pChar in m:
            if sWord in wordSet:
                return False
            else:
                m[pChar] = sWord
        else:
            if m[pChar] != sWord:
                return False

    return pIndex == pLength and sIndex == sLength

