#!/usr/bin/python3

def compareVersion(version1, version2):
    splitV1s = version1.split('.')
    splitV2s = version2.split('.')

    i1 = 0
    i2 = 0

    while i1 < len(splitV1s) and i2 < len(splitV2s):
        partNum1 = int(splitV1s[i1])
        partNum2 = int(splitV2s[i2])
        if partNum1 < partNum2:
            return -1
        elif partNum1 > partNum2:
            return 1
        else:
            i1 += 1
            i2 += 1
    
    while i1 < len(splitV1s):
        partNum1 = int(splitV1s[i1])
        if partNum1 != 0:
            return 1
        i1 += 1
    while i2 < len(splitV2s):
        partNum2 = int(splitV2s[i2])
        if partNum2 != 0:
            return -1
        i2 += 1
    return 0
