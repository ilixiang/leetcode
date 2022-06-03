#!/usr/bin/python3

def longestPalindrome(s):
    processedS = '#' + '#'.join(list(s)) + '#'
    center = -1
    rightBoudary = -1
    radiuses = []
    maxRadiusCenter = 0
    for index in range(0, len(processedS)):
        radius = 1
        if index > rightBoudary:
            while index + radius < len(processedS) and index - radius > -1 and processedS[index + radius] == processedS[index - radius]:
                radius = radius + 1
        else:
            symmetricIndex = 2 * center - index
            leftBoudary = 2 * center - rightBoudary
            if symmetricIndex + 1 - radiuses[symmetricIndex] == leftBoudary:
                radius = rightBoudary - index + 1
                while index + radius < len(processedS) and index - radius > -1 and processedS[index + radius] == processedS[index - radius]:
                    radius = radius + 1
            else:
                radius = radiuses[symmetricIndex] if radiuses[symmetricIndex] <= symmetricIndex - leftBoudary + 1 else symmetricIndex - leftBoudary + 1
        radiuses.append(radius)
        if radius + index - 1 > rightBoudary:
            rightBoudary = radius + index - 1
            center = index
        maxRadiusCenter = maxRadiusCenter if radiuses[maxRadiusCenter] >= radius else index
    maxRadius = radiuses[maxRadiusCenter]
    leftIndex = (maxRadiusCenter - maxRadius + 1) // 2
    rightIndex = (0 if (maxRadiusCenter + maxRadius - 2) // 2 == -1 else (maxRadiusCenter + maxRadius - 2) // 2)  + 1
    return s[leftIndex:rightIndex]

print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))

