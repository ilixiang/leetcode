#!/usr/bin/python3

def convert(s, numRows):
    if numRows == 1:
        return s
    
    length = len(s)
    cycle = 2 * numRows - 2
    cycleCount = length // cycle + 1
    tmp = []
    for i in range(0, numRows):
        for j in range(0, cycleCount):
            first = cycle * j + i
            second = cycle * j + cycle - i
            if first < length:
                tmp.append(s[first])
            if i != 0 and i != numRows - 1 and second < length:
                tmp.append(s[second])
    return ''.join(tmp)
