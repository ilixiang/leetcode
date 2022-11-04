#!/usr/bin/python3

def fullJustify(words, maxWidth):
    i = 0
    start = 0
    remainWidth = maxWidth
    wordCount = 0
    wordLength = 0
    res = []
    while i < len(words):
        word = words[i]
        if remainWidth >= len(word):
            wordCount += 1
            wordLength += len(word)
            remainWidth -= len(word)
            if remainWidth != 0:
                remainWidth -= 1
            i += 1
        else:
            if wordCount == 1:
                res.append(words[start] + ' ' * (maxWidth - wordLength))
            else:
                tmp = []
                space = maxWidth - wordLength
                leastSpace = space // (wordCount - 1)
                extraSpace = space % (wordCount - 1)
                for j in range(start, i - 1):
                    tmp.append(words[j])
                    if extraSpace != 0:
                        tmp.append(' ' * (leastSpace + 1))
                        extraSpace -= 1
                    else:
                        tmp.append(' ' * leastSpace)
                tmp.append(words[i - 1])
                res.append(''.join(tmp))
            wordCount = 0
            wordLength = 0
            remainWidth = maxWidth
            start = i
    if wordCount != 0:
        tmp = []
        space = maxWidth - wordLength
        remainSpace = space
        for j in range(start, i - 1):
            tmp.append(words[j])
            tmp.append(' ')
            remainSpace -= 1
        tmp.append(words[i - 1])
        if remainSpace != 0:
            tmp.append(' ' * remainSpace)
        res.append(''.join(tmp))
    return res
