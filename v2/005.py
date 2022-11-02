#!/usr/bin/python3

def longestPalindrome(s):
    if len(s) <= 1:
        return s

    processedS = '#' + '#'.join(list(s)) + '#'
    length = len(processedS)
    maxRadiusCenter = 0
    maxRadius = 0
    radiuses = [0] * length

    for center in range(0, len(processedS)):
        maxCoveredIndex = maxRadius + maxRadiusCenter
        if center >= maxCoveredIndex:
            radius = 0
            while center + radius < length \
                and center - radius >= 0 \
                    and processedS[center + radius] == processedS[center - radius]:
                radius += 1
            radius -= 1
            maxRadius = radius
            maxRadiusCenter = center
            radiuses[center] = radius
        else:
            symmetricalCenter = 2 * maxRadiusCenter - center
            symmetricalCenterRadius = radiuses[symmetricalCenter]
            if center + symmetricalCenterRadius != maxCoveredIndex:
                radiuses[center] = min(symmetricalCenterRadius, maxCoveredIndex - center)
            elif center + symmetricalCenterRadius == maxCoveredIndex:
                radius = symmetricalCenterRadius
                while center + radius < length \
                    and center - radius >= 0 \
                        and processedS[center + radius] == processedS[center - radius]:
                    radius += 1
                radius -= 1
                maxRadius = radius
                maxRadiusCenter = center
                radiuses[center] = radius
    
    maxRadiusCenter = 0
    for i in range(0, length):
        if radiuses[i] > radiuses[maxRadiusCenter]:
            maxRadiusCenter = i
    maxRadius = radiuses[maxRadiusCenter]
    return s[(maxRadiusCenter - maxRadius) // 2: (maxRadiusCenter + maxRadius) // 2]

