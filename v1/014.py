#!/usr/bin/python3

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]

    arr = []
    cIndex = 0
    while cIndex < len(strs[0]):
        for sIndex in range(1, len(strs)):
            if cIndex >= len(strs[sIndex]) or strs[sIndex][cIndex] != strs[0][cIndex]:
                return ''.join(arr)
        arr.append(strs[0][cIndex])
        cIndex = cIndex + 1
    return ''.join(arr)

print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['dog', 'racecar', 'car']))

