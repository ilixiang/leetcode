#!/usr/bin/python3

def strStr(haystack, needle):
    if needle == None or len(needle) == 0:
        return 0
    needleLength = len(needle)
    if haystack == None or len(haystack) < needleLength:
        return -1
    haystackLength = len(haystack)
    
    step = [0]
    for i in range(1, needleLength + 1):
        maxCount = 0
        for j in range(i - 1, 0, -1):
            k = 0
            while k < j and needle[k] == needle[i - j + k]:
                k = k + 1
            if k == j:
                maxCount = k
                break
        step.append(maxCount)
    haystackIndex = 0
    matched = 0
    while haystackIndex + needleLength <= haystackLength:
        while matched < needleLength and needle[matched] == haystack[haystackIndex + matched]:
            matched = matched + 1
        if matched == needleLength:
            return haystackIndex
        if matched == 0:
            haystackIndex = haystackIndex + 1
        else:
            haystackIndex = haystackIndex + matched - step[matched]
            matched = step[matched]
    return -1
            

print(strStr('babbbbbabb', 'bbab'))
