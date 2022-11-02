#!/usr/bin/python3

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''

    if len(strs) == 1:
        return strs[0]

    tmp = []
    firstStr = strs[0]
    for i in range(0, len(firstStr)):
        c = firstStr[i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or c != strs[j][i]:
                return ''.join(tmp)
        tmp.append(c)
    return ''.join(tmp)

