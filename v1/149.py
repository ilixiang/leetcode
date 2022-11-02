#!/usr/bin/python3

def maxPoints(points):
    result = 1
    for i in range(0, len(points)):
        m = {}
        for j in range(i + 1, len(points)):
            (numerator, denominator) = getSlope(points[i], points[j])
            print(points[i], points[j], numerator, denominator)
            if not numerator in m:
                m[numerator] = {}
            if not denominator in m[numerator]:
                m[numerator][denominator] = 1
            m[numerator][denominator] = m[numerator][denominator] + 1
            result = max(result, m[numerator][denominator])
    return result

def getSlope(pointA, pointB):
    xDiff = pointB[0] - pointA[0]
    yDiff = pointB[1] - pointA[1]

    positive = (xDiff > 0 and yDiff > 0) or (xDiff < 0 and yDiff < 0)
    xDiff = abs(xDiff)
    yDiff = abs(yDiff)
    maxDiff = max(xDiff, yDiff)
    minDiff = min(xDiff, yDiff)
    if minDiff == 0:
        return (0, 0)
    while maxDiff % minDiff != 0:
        remainder = maxDiff % minDiff
        maxDiff = minDiff
        minDiff = remainder
    return (xDiff // minDiff if positive else -1 * xDiff / minDiff, yDiff // minDiff)

print(maxPoints([[1,1],[2,2],[3,3]]))
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

