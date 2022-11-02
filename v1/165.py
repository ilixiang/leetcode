#!/usr/bin/python3

def compareVersion(version1, version2):
    segments1 = version1.split('.')
    segments2 = version2.split('.')

    i = 0
    while i < len(segments1) and i < len(segments2):
        v1 = int(segments1[i])
        v2 = int(segments2[i])
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        i += 1

    while i < len(segments1):
        v1 = int(segments1[i])
        if v1 != 0:
            return 1
        i += 1

    while i < len(segments2):
        v2 = int(segments2[i])
        if v2 != 0:
            return -1
        i += 1
    return 0

print(compareVersion('1.01', '1.001'))
print(compareVersion('1.0', '1.0.0'))
print(compareVersion('0.1', '1.1'))

