#!/usr/bin/python3

def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]

    i = 0
    while i < len(strs[0]):
        c = strs[0][i]
        for j in range(1, len(strs)):
            str = strs[j]
            if i >= len(str) or str[i] != c:
                return strs[0][0:i]
        i += 1
    return strs[0]
