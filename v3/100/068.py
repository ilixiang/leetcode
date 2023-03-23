#!/usr/bin/python3

def fullJustify(words, maxWidth):
    rev = []
    wordWidth = 0
    l, r = 0, 0
    while r < len(words):
        if wordWidth + len(words[r]) + r - l > maxWidth:
            spaceWidth = maxWidth - wordWidth
            if l == r - 1:
                rev.append(words[l] + ' ' * spaceWidth)
            else:
                intervalNum = r - l - 1
                avgSpaceWidth = spaceWidth // intervalNum
                extraSpaceWidth = spaceWidth % intervalNum
                tmp = []
                for i in range(l, r - 1):
                    tmp.append(words[i])
                    if extraSpaceWidth != 0:
                        tmp.append(' ' * (avgSpaceWidth + 1))
                        extraSpaceWidth -= 1
                    else:
                        tmp.append(' ' * avgSpaceWidth)
                tmp.append(words[r - 1])
                rev.append(''.join(tmp))
            wordWidth = len(words[r])
            l = r
        else:
            wordWidth += len(words[r])
        r += 1

    tmp = []
    endSpaceWidth = maxWidth
    for i in range(l, r - 1):
        tmp.append(words[i])
        tmp.append(' ')
        endSpaceWidth = endSpaceWidth - len(words[i]) - 1
    tmp.append(words[r - 1])
    endSpaceWidth = endSpaceWidth - len(words[r - 1])
    print(endSpaceWidth)
    tmp.append(' ' * endSpaceWidth)
    rev.append(''.join(tmp))

    return rev
