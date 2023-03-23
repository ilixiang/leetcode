#!/usr/bin/python3

import math

def maxPoints(points):
    def greatCommonDivisor(a, b):
        if a > b:
            a, b = b, a
        while a != 0:
            b %= a
            a, b = b, a
        return b

    def calcLineProperty(a, b):
        [ax, ay] = a
        [bx, by] = b
        xDiff = ax - bx
        yDiff = ay - by
        interceptNumerator = ax * by - bx * ay
        interceptDenuminator = ax - bx

        if xDiff == 0:
            return (0, 1, 0, ax)

        if yDiff == 0:
            return (1, 0, 1, ay)

        slopeDivisor = greatCommonDivisor(abs(xDiff), abs(yDiff))
        if slopeDivisor * xDiff < 0:
            slopeDivisor *= -1
        
        interceptDivisor = greatCommonDivisor(abs(interceptDenuminator), abs(interceptNumerator))
        if interceptDivisor * interceptDenuminator < 0:
            interceptDivisor *= -1

        return (xDiff // slopeDivisor, yDiff // slopeDivisor, interceptDenuminator // interceptDivisor, interceptNumerator // interceptDivisor)

    rev = 0
    m = {}
    for i in range(len(points)):
        a = points[i]
        for j in range(i + 1, len(points)):
            b = points[j]
            lineProperty = calcLineProperty(a, b)
            originalCount = m.get(lineProperty, 0)
            m[lineProperty]=  originalCount + 2
            rev = max(rev, originalCount + 2)
    return int(math.sqrt(rev)) + 1
