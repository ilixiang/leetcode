#!/usr/bin/python3

def maxPoints(points):
    length = len(points)
    if length == 1:
        return 1

    def reduceFracetion(numerator, denominator):
        if numerator == 0:
            return (0, 1)
        positive = (numerator >= 0 and denominator > 0) or (numerator <= 0 and denominator < 0)
        m = max(abs(numerator), abs(denominator))
        n = min(abs(numerator), abs(denominator))
        while m % n != 0:
            m, n = n, m % n
        if positive:
            return (abs(numerator // n), abs(denominator // n))
        else:
            return (-1 * abs(numerator // n), abs(denominator // n))

    m = {}
    for i in range(0, length):
        p1 = points[i]
        [p1x, p1y] = p1 
        for j in range(i + 1, length):
            p2 = points[j]
            [p2x, p2y] = p2
            key = None
            if p1x == p2x:
                key = 'INF' + str(p1x)
            elif p1y == p2y:
                key = 'ZERO' + str(p1y)
            else:
                (slopeNumerator, slopeDenominator) = reduceFracetion(p1y - p2y, p1x - p2x)
                (interceptNumerator, interceptDenominator) = reduceFracetion(p1x * p2y - p2x * p1y, p1x - p2x)
                key = str(slopeNumerator) + '/' + str(slopeDenominator) +\
                    '&' + str(interceptNumerator) + '/' + str(interceptDenominator)
            if not key in m:
                m[key] = set([(p1x, p1y), (p2x, p2y)])
            else:
                m[key].update([(p1x, p1y), (p2x, p2y)])
        
    maxCount = 0
    for key in m:
        keyPointSet = m[key]
        if len(keyPointSet) > maxCount:
            maxCount = len(keyPointSet)
    return maxCount
