#!/usr/bin/python3

def strStr(haystack, needle):
    lps = [0] * (len(needle) + 1)

    for subLength in range(2, len(needle)):
        if needle[lps[subLength - 1]] == needle[subLength - 1]:
            lps[subLength] = lps[subLength - 1] + 1
            continue

        for subsubLength in range(lps[subLength - 1], 0, -1):
            i = 0
            while i < subsubLength and needle[i] == needle[subLength - subsubLength + i]:
                i += 1
            if i == subsubLength:
                lps[subLength] = subsubLength
                break

    print(lps)
    i = 0
    matchedLength = 0
    while i < len(haystack):
        while i < len(haystack) and matchedLength < len(needle) and haystack[i] == needle[matchedLength]:
            i += 1
            matchedLength += 1

        if matchedLength == len(needle):
            return i - matchedLength
        elif matchedLength == 0:
            i += 1
        else:
            matchedLength = lps[matchedLength]
    return -1

if __name__ == '__main__':
    strStr('mississippi', 'issip')
