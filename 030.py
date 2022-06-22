#!/usr/bin/python3

def findSubstring(s, words):
    if len(words) == 0:
        return []
    wordLength = len(words[0])
    if len(s) < wordLength * len(words):
        return []

    wordMap = {}
    for wIndex in range(0, len(words)):
        word = words[wIndex]
        if word in wordMap:
            wordMap[word].add(wIndex)
        else:
            wordMap[word] = set([wIndex])

    result = []
    exists = [False] * len(words)
    queue = []
    for wIndex in range(0, wordLength):
        sIndex = wIndex
        while sIndex <= len(s) - wordLength:
            comparator = s[sIndex: sIndex + wordLength]
            if comparator in wordMap:
                wordIndexSet = wordMap[comparator]
                nonEmptyIndex = True
                for emptyIndex in wordIndexSet:
                    if not exists[emptyIndex]:
                        queue.append(emptyIndex)
                        exists[emptyIndex] = True
                        sIndex = sIndex + wordLength
                        nonEmptyIndex = False 
                        if len(queue) == len(words):
                            result.append(sIndex - wordLength * len(words))
                        break
                if nonEmptyIndex:
                    queueIndex = queue.pop(0)
                    exists[queueIndex] = False
                    while not queueIndex in wordIndexSet:
                        queueIndex = queue.pop(0)
                        exists[queueIndex] = False
                    queue.append(queueIndex)
                    exists[queueIndex] = True
                    sIndex = sIndex + wordLength
                    if len(queue) == len(words):
                        result.append(sIndex - wordLength * len(words))
            else:
                sIndex = sIndex + wordLength
                for eIndex in range(0, len(words)):
                    exists[eIndex] = False
                queue.clear()
        queue.clear()
        for eIndex in range(0, len(words)):
            exists[eIndex] = False
    return result

print(findSubstring('barfoothefoobarman', ['foo', 'bar']))
print(findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']))
print(findSubstring('barfoofoobarthefoobarman', ['bar', 'foo', 'the']))
print(findSubstring('aaaaaaaaaaaaaa', ['aa','aa']))

