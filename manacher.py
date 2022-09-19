#!/usr/bin/python3

def longestPalindrome(s):
    if len(s) == 0:
        return ''
    processedS = '#' + '#'.join(list(s)) + '#'
    processedLen = len(processedS)
    radiuses = [None] * processedLen
    radiuses[0] = 0
    center = 0
    radius = 0
    maxRadiusIndex = 0
    for i in range(1, processedLen):
        coveredRightIndex = center + radius
        coveredLeftIndex = center - radius
        if i >= coveredRightIndex:
            left = i - 1
            right = i + 1
            while left >= 0 and right < processedLen and processedS[left] == processedS[right]:
                left = left - 1
                right = right + 1
            center = i
            radius = right - i - 1
            radiuses[i] = radius
            maxRadiusIndex = i if radius > radiuses[maxRadiusIndex] else maxRadiusIndex
        else:
            symmetric = 2 * center - i
            symmetricRadius = radiuses[symmetric]
            symmetricLeftIndex = symmetric - symmetricRadius
            if symmetricLeftIndex < coveredLeftIndex:
                radiuses[i] = coveredRightIndex - i
            elif symmetricLeftIndex > coveredLeftIndex:
                radiuses[i] = symmetricRadius
            else:
                left = 2 * i - coveredRightIndex - 1
                right = coveredRightIndex + 1
                while left >= 0 and right < processedLen and processedS[left] == processedS[right]:
                    left = left - 1
                    right = right + 1
                center = i
                radius = right - i - 1
                radiuses[i] = radius
                maxRadiusIndex = i if radius > radiuses[maxRadiusIndex] else maxRadiusIndex
    left = (maxRadiusIndex - radiuses[maxRadiusIndex]) // 2
    right = (maxRadiusIndex + radiuses[maxRadiusIndex]) // 2
    print(radiuses)
    return s[left:right]

print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
