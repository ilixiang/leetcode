#!/usr/bin/python3

def fullJustify(words, maxWidth):
    letterCount = 0
    lastIndex = 0
    index = 0
    arr = []
    while index < len(words):
        if letterCount + len(words[index]) + index - lastIndex <= maxWidth:
            letterCount = letterCount + len(words[index])
        else:
            tmp = []
            slotCount = index - lastIndex - 1
            if slotCount == 0:
                tmp.append(words[lastIndex])
                tmp.append(' ' * (maxWidth - letterCount))
            else:
                averageSlotSize = (maxWidth - letterCount) // slotCount
                remainSlotSize = (maxWidth - letterCount) % slotCount
                arrangedWordCount = 0
                while arrangedWordCount < slotCount:
                    tmp.append(words[lastIndex + arrangedWordCount])
                    tmp.append(' ' * ((averageSlotSize + 1) if arrangedWordCount < remainSlotSize else averageSlotSize))
                    arrangedWordCount = arrangedWordCount + 1
                tmp.append(words[lastIndex + arrangedWordCount])
            arr.append(tmp)
            letterCount = len(words[index])
            lastIndex = index
        index = index + 1

    tmp = []
    lastSpaceSize = maxWidth - letterCount - index + lastIndex + 1
    tmp.append(words[lastIndex])
    lastIndex = lastIndex + 1
    while lastIndex < index:
        tmp.append(' ')
        tmp.append(words[lastIndex])
        lastIndex = lastIndex + 1
    tmp.append(' ' * lastSpaceSize)
    arr.append(tmp)

    return list(map(lambda a: ''.join(a), arr))

print(fullJustify(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16))
print(fullJustify(['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], 16))

